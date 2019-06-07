import argparse
import gitnotes
import os

parser = argparse.ArgumentParser(description='Retrive Git commit as release notes.')
parser.add_argument('-p', '--path', type=str, required=True,
                    help='The path to the folder)')
parser.add_argument('-k', '--key', type=str, required=True,
                    help='The Story/Project id/key from Jira)')
parser.add_argument('-c', '--c_count', type=str,
                    help='The count of commits to search for)')

args = parser.parse_args()
git_notes = gitnotes.GitNotes(args)