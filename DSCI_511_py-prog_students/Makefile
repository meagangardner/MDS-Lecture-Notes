book:
	cp README.md jupyter-book/README.md
	jupyter-book build jupyter-book
	rm -rf jupyter-book/_build/html/.nojekyll
	cp -r jupyter-book/_build/html/* jupyter-book/
	if [ ! -f "jupyter-book/.nojekyll" ]; then touch jupyter-book/.nojekyll; fi

clean-book:
	rm -rf jupyter-book/_build
	rm -rf jupyter-book/*.html
	rm -rf jupyter-book/_static
	rm -rf jupyter-book/_images