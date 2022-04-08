NAME = tau-starship

VERSION := $(shell awk '/Version:/ { print $$2 }' $(NAME).spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' $(NAME).spec | sed 's|%{?dist}||g')
TAG=$(NAME)-$(VERSION)

all: archive

tag:
	@git tag -a -f -m "Tag as $(TAG)" -f $(TAG)
	@echo "Tagged as $(TAG)"

archive: tag
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD > $(TAG).tar
	@gzip -f $(TAG).tar
	@echo "$(TAG).tar.gz created" 
	@sha1sum $(TAG).tar.gz > $(TAG).sha1sum