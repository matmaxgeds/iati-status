#!/bin/sh

setup_git() {
  git config --global user.email "deploy@travis-ci.org"
  git config --global user.name "Code for IATI bot"
  git clone --branch gh-pages https://${GITHUB_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git deploy
}

commit_website_files() {
  mv _site/* deploy/
  cd deploy
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push
}

setup_git
commit_website_files
upload_files
