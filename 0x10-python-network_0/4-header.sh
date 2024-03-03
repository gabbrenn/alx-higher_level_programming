#!/bin/bash
#takes in a URL as an argument
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
