JEKYLL=bundle exec jekyll
JOPTS= #--trace --verbose
DEVCONF=--config _config.yml,_config_dev.yml
serve:
	${JEKYLL} serve ${JOPTS} ${DEVCONF}

draft:
	${JEKYLL} serve ${JOPTS} ${DEVCONF} --draft --future

build:
	${JEKYLL} build

clean:
	rm -fr _site/
