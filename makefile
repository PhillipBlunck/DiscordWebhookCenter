######################################################################################
##                                                                                  ##
## Makefile for Discord Webhook Center                                              ##
##                                                                                  ##
## Phillip Blunck, 2020-10-06                                                       ##
##                                                                                  ##
######################################################################################

PACKAGES := python3 python3-pip
PIPPACKAGES := discord-webhook

######################################################################################

prepare:
	@ for PACKAGE in $(PACKAGES); do \
	dpkg --status $$PACKAGE 1>/dev/null 2>/dev/null || \
	sudo apt install --yes $$PACKAGE; done
	@ for PIPPACKAGE in $(PIPPACKAGES); do \
	pip3 show $$PIPPACKAGE 1>/dev/null 2>/dev/null || \
	sudo pip3 install --quiet $$PIPPACKAGE; done
	@ touch $@

install: prepare
	@ sh generate_settings.sh > settings.json
	@ touch $@

start: install
	python3 DiscordWebhookCenter.py

clean:
	rm -rf __pycache__

distclean: clean
	rm -rf settings.json
	rm -rf install
	rm -rf prepare

######################################################################################
