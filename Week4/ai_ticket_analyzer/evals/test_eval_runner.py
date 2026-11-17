import unittest
from unittest.mock import patch

from ai_analyzer.schemas import TicketAnalysis

from . import run_evals


class TestEvaluationRunner(unittest.TestCase):

    def make_mock_results(self):

        mock_results = [
            TicketAnalysis(
                category="mechanical",
                priority="critical",
                summary="The CNC spindle has seized and production has stopped",
            ),
            TicketAnalysis(
                category="electrical",
                priority="medium",
                summary="The control panel display flickers several times per shift, temporarily preventing the operator from reading machine information. Restarting the display restores normal operation, but interrupts the operator's work.",
            ),
            TicketAnalysis(
                category="other",
                priority="low",
                summary="Wrong-colored machine enclosure.",
            ),
            TicketAnalysis(
                category="software",
                priority="high",
                summary="Repeated loss of tool offsets causing major delays",
            ),
            TicketAnalysis(
                category="mechanical",
                priority="low",
                summary="The coolant pump makes unusual noise; machine works normally.",
            ),
        ]

        return mock_results
    
    def test_success(self):

        mock_results = self.make_mock_results()

        with patch("evals.run_evals.analyze_ticket") as mock_analyze:
            mock_analyze.side_effect = mock_results

            with self.assertRaises(SystemExit) as captured:
                run_evals.main()

            self.assertEqual(captured.exception.code, 0)


    def test_wrong_classifications(self):

        mock_result = TicketAnalysis(
            category="mechanical",
            priority="critical",
            summary="The CNC spindle has seized, stopping production.",
        )

        with patch("evals.run_evals.analyze_ticket") as mock_analyze:
            mock_analyze.return_value = mock_result
        
            with self.assertRaises(SystemExit) as captured:
                run_evals.main()

            self.assertEqual(captured.exception.code, 1)


    def test_api_failure(self):
        mock_api_failure_results = self.make_mock_results()
        mock_api_failure_results[4] = None

        with patch("evals.run_evals.analyze_ticket") as mock_analyze:
            mock_analyze.side_effect = mock_api_failure_results

            with self.assertRaises(SystemExit) as captured:
                run_evals.main()

            self.assertEqual(captured.exception.code, 1)


