from typing import List

import click

from lhotse.bin.modes import download, prepare
from lhotse.recipes.fleurs import download_fleurs, prepare_fleurs
from lhotse.utils import Pathlike


@prepare.command(context_settings=dict(show_default=True))
@click.argument("corpus_dir", type=click.Path(exists=True, dir_okay=True))
@click.argument("output_dir", type=click.Path())
@click.option(
    "-l",
    "--language",
    default=["auto"],
    multiple=True,
    help="Languages to prepare (scans CORPUS_DIR for language codes by default).",
)
@click.option(
    "-s",
    "--split",
    default=["train", "dev", "test"],
    multiple=True,
    help="Splits to prepare (available options: train, dev, test, validated, invalidated, other)",
)
@click.option(
    "-j",
    "--num-jobs",
    type=int,
    default=1,
    help="How many threads to use (can give good speed-ups with slow disks).",
)
def fleurs(
    corpus_dir: Pathlike,
    output_dir: Pathlike,
    language: List[str],
    split: List[str],
    num_jobs: int,
):
    """
    Fleurs manifest preparation script.
    CORPUS_DIR is expected to contain sub-directories that are named with Fleurs language codes,
    e.g., "en", "pl", etc.
    """
    languages = language[0] if len(language) == 1 else language
    prepare_fleurs(
        corpus_dir=corpus_dir,
        languages=languages,
        splits=split,
        output_dir=output_dir,
        num_jobs=num_jobs,
    )


@download.command(context_settings=dict(show_default=True))
@click.argument("target_dir", type=click.Path())
@click.option(
    "-l",
    "--languages",
    default="all",
    help="Languages to prepare (scans CORPUS_DIR for language codes by default).",
)
def fleurs(
    target_dir: Pathlike,
    languages: List[str],
) -> None:
    """Fleurs download."""
    download_fleurs(
        target_dir=target_dir,
        languages=languages,
    )