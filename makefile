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
	@ touch $&

install: prepare
	@ .\generate_settings.sh > test.txt
	@ touch $&

start: python3 DiscordWebhookClient.py

clean:
	rm -rf __pycache__

distclean: clean
	rm settings.json

######################################################################################
