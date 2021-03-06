#!/bin/sh

export LANG=en_US.UTF-8

git secrets --pre_commit_hook -- "$@"

git diff --cached --name-status | grep \.py$ | while read st file; do
        # skip deleted files
        if [ "$st" == 'D' ]; then continue; fi

        pylint --rcfile=.pylintrc $file

        ret=$?
        if [ $ret -ne 0 ]; then
                exit $ret
        fi

        flake8 $file

        ret=$?
        if [ $ret -ne 0 ]; then
                exit $ret
        fi
done
