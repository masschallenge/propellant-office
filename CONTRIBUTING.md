# Contributing

The MassChallenge team owns and maintains Propellant and decides what goes into each release.
Changes come through pull requests that a maintainer reviews and merges.

## Design comes first

Any new template, layout or visual change starts as an approved design, made in a design tool such
as Figma or Claude Design, before any code is written. The pull request is desk checked against
that design, and the review by the MassChallenge design lead is the final check before it is
merged. Link the design in the pull request.

## How contributions work

- **Bug reports and questions are welcome.** Open an issue with what you expected and what you saw.
- **Ideas for new templates start as an issue**, so we can agree on them before anyone builds.
- **Brand changes** to the logo, colors, fonts or voice come from the MassChallenge brand team, and
  land in [propellant-web](https://github.com/masschallenge/propellant-web) first.
- **Security problems** are never reported in a public issue. Follow [SECURITY.md](SECURITY.md).

## Making a change

1. Create a branch.
2. Install the build tools with `python3 -m pip install -r requirements.txt`.
3. Change the guides in `docs` or the generator in `scripts`. Never edit the files in `templates`
   by hand: they are rebuilt from the scripts.
4. Run `python3 scripts/build_templates.py` and `python3 -m unittest discover -s tests`.
5. Open each changed template in Word, PowerPoint or Excel, and in Google Workspace, and look at
   every page before you commit.
6. Add an entry to `CHANGELOG.md` and open a pull request that explains why the change is needed.

## Standards

- Write like the rest of Propellant: plain words, short sentences, sentence case, and no em dashes
  or en dashes.
- Every claim about how Office or Google Workspace works links to the vendor's own documentation.
- Descriptive names and no comments in the scripts. Every change to the generator comes with tests.
- Commit messages describe why, not just what.
