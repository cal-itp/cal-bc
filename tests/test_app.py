import pytest
from pathlib import Path

from typer.testing import CliRunner

from cal_bc.app import app


class TestApp:
    @pytest.fixture
    def runner(self) -> CliRunner:
        return CliRunner()

    def test_list(self, runner: CliRunner):
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "cal-bc-8-1-sketch" in result.output
        assert "Cal-B/C Sketch v8.1" in result.output

    def test_download(self, runner: CliRunner):
        result = runner.invoke(app, ["download"])
        assert result.exit_code == 2

    @pytest.mark.vcr
    def test_download_specific_version(self, tmp_path: Path, runner: CliRunner):
        result = runner.invoke(
            app, ["download", "cal-bc-8-1-sketch", "--output-dir", tmp_path]
        )
        assert result.exit_code == 0
        assert "cal-bc-8-1-sketch.xlsm" in result.output
        assert (tmp_path / "cal-bc-8-1-sketch.xlsm").exists()

    @pytest.mark.vcr
    def test_complete(self, tmp_path: Path, runner: CliRunner):
        result = runner.invoke(
            app, ["download", "cal-bc-8-1-sketch", "--output-dir", tmp_path]
        )
        assert result.exit_code == 0
        result = runner.invoke(
            app,
            [
                "complete",
                str(tmp_path / "cal-bc-8-1-sketch.xlsm"),
                "--cell",
                "ProjName",
                "--value",
                "Testing Project",
            ],
        )
        assert result.exit_code == 0
        assert (tmp_path / "cal-bc-8-1-sketch-complete.xlsm").exists()

    @pytest.mark.vcr
    def test_evaluate(self, tmp_path: Path, runner: CliRunner):
        result = runner.invoke(
            app, ["download", "cal-bc-8-1-sketch", "--output-dir", tmp_path]
        )
        assert result.exit_code == 0
        result = runner.invoke(
            app,
            [
                "complete",
                str(tmp_path / "cal-bc-8-1-sketch.xlsm"),
                "--cell",
                "ProjName",
                "--value",
                "Testing Project",
            ],
        )
        assert result.exit_code == 0
        result = runner.invoke(
            app,
            [
                "evaluate",
                str(tmp_path / "cal-bc-8-1-sketch-complete.xlsm"),
                "--cell",
                "ProjName",
            ],
        )
        assert result.exit_code == 0
        assert "Testing Project" in result.output
