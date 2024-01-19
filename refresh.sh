#!/usr/bin/sh

cp new.xspf ~/.mpd/music/playlists
mpc clear
mpc load playlists/new.xspf
