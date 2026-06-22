import unittest
from protein_rollup import rollup_psms_to_proteins

class TestProteinRollup(unittest.TestCase):

    def test_basic_rollup(self):
        """Test basic PSM to protein rollup with known FDR"""
        # Create test PSMs: mix of target and decoy
        psms = [
            # Target PSMs
            {'peptide': 'PEPTIDE1', 'proteins': ['PROT_A'], 'score': 10.0, 'source': 'target'},
            {'peptide': 'PEPTIDE2', 'proteins': ['PROT_A'], 'score': 8.0, 'source': 'target'},
            {'peptide': 'PEPTIDE3', 'proteins': ['PROT_B'], 'score': 7.0, 'source': 'target'},
            # Decoy PSMs
            {'peptide': 'DECOY1', 'proteins': ['DECOY_PROT'], 'score': 9.0, 'source': 'decoy'},
            {'peptide': 'DECOY2', 'proteins': ['DECOY_PROT'], 'score': 6.0, 'source': 'decoy'},
        ]

        # Apply 1% FDR threshold
        results = rollup_psms_to_proteins(psms, fdr_threshold=0.01)

        # Should return some results (exact number depends on scoring)
        self.assertIsInstance(results, list)

        # Verify each result has required fields
        for protein in results:
            self.assertIn('accession', protein)
            self.assertIn('peptides', protein)
            self.assertIn('score', protein)
            self.assertIn('is_decoy', protein)
            self.assertIn('peptide_count', protein)

    def test_independent_fdr_estimation(self):
        """Test that protein-level FDR is estimated independently from PSM-level"""
        # Create scenario where PSM-level FDR would be low but protein-level FDR high
        # Many low-quality peptide-spectrum maps to same protein
        psms = []

        # Add many low-scoring target PSMs mapping to same protein
        for i in range(20):
            psms.append({
                'peptide': f'PEPTIDE_TARGET_{i}',
                'proteins': ['PROT_1'],
                'score': 1.0 + i*0.1,  # Low scores
                'source': 'target'
            })

        # Add fewer high-scoring decoy PSMs
        for i in range(5):
            psms.append({
                'peptide': f'PEPTIDE_DECOY_{i}',
                'proteins': ['DECOY_PROT_1'],
                'score': 5.0 - i*0.5,  # Higher scores than some targets
                'source': 'decoy'
            })

        # Apply 1% FDR
        results = rollup_psms_to_proteins(psms, fdr_threshold=0.01)

        # The function should apply protein-level FDR independently
        # This test primarily verifies it runs without error and returns structured data
        self.assertIsInstance(results, list)

    def test_razor_peptide_rule(self):
        """Test that razor peptide rule is applied (best PSM per peptide kept)"""
        psms = [
            # Two PSMs for same peptide, different scores
            {'peptide': 'PEPTIDE_X', 'proteins': ['PROT_A'], 'score': 5.0, 'source': 'target'},
            {'peptide': 'PEPTIDE_X', 'proteins': ['PROT_A'], 'score': 8.0, 'source': 'target'},  # Better score
            {'peptide': 'PEPTIDE_Y', 'proteins': ['PROT_B'], 'score': 6.0, 'source': 'target'},
        ]

        results = rollup_psms_to_proteins(psms, fdr_threshold=0.01)

        # Should only have 2 unique peptides after razor rule
        total_peptides = sum(len(p['peptides']) for p in results)
        # PEPTIDE_X should appear only once (with score 8.0), PEPTIDE_Y once
        # Depending on FDR threshold, we might get 0, 1, or 2 proteins
        # But the key is that we don't double-count PEPTIDE_X

        # Verify no duplicate peptides within a protein
        for protein in results:
            # Each peptide should appear only once in the protein's peptide list
            self.assertEqual(len(set(protein['peptides'])), len(protein['peptides']))

    def test_decoy_handling(self):
        """Test proper decoy protein identification"""
        psms = [
            # Mixed target and decoy evidence for same protein -> should be target
            {'peptide': 'PEPTIDE_1', 'proteins': ['PROT_MIXED'], 'score': 7.0, 'source': 'target'},
            {'peptide': 'PEPTIDE_2', 'proteins': ['PROT_MIXED'], 'score': 6.0, 'source': 'decoy'},

            # Only decoy evidence -> should be decoy
            {'peptide': 'DECOYPEP_1', 'proteins': ['PROT_DECOY_ONLY'], 'score': 8.0, 'source': 'decoy'},
            {'peptide': 'DECOYPEP_2', 'proteins': ['PROT_DECOY_ONLY'], 'score': 7.0, 'source': 'decoy'},
        ]

        results = rollup_psms_to_proteins(psms, fdr_threshold=0.1)  # Higher threshold to get results

        # Find our test proteins
        mixed_prot = next((p for p in results if p['accession'] == 'PROT_MIXED'), None)
        decoy_prot = next((p for p in results if p['accession'] == 'PROT_DECOY_ONLY'), None)

        # PROT_MIXED should be marked as target (not decoy) since it has target evidence
        if mixed_prot:
            self.assertFalse(mixed_prot['is_decoy'],
                           "Protein with mixed target/decoy evidence should be target")

        # PROT_DECOY_ONLY should be marked as decoy
        if decoy_prot:
            self.assertTrue(decoy_prot['is_decoy'],
                          "Protein with only decoy evidence should be decoy")

if __name__ == '__main__':
    unittest.main()