book:
	cp README.md jupyter-book/README.md
	jupyter-book build jupyter-book
	if [ ! -d "docs" ]; then mkdir docs; fi
	if [ ! -f ".nojekyll" ]; then touch docs/.nojekyll; fi
	cp -r jupyter-book/_build/html/* docs

clean-book:
	rm -rf docs/*
	rm -rf jupyter-book/_build/*