#!/bin/bash

LDBC_BASE_URL=https://raw.githubusercontent.com/maxhbr/LDBcollector/generated/flict/
LDBC_JSON_FILE=translation.json
LDBC_BASE_URL=${LDBC_BASE_URL}/${LDBC_JSON_FILE}
ALIAS_REPORT_MD=alias-report.md
ALIAS_REPORT_PDF=alias-report.pdf

FLICT_TRANSLATION=flict-translations.json

if [ ! -f ${LDBC_JSON_FILE} ]
then
    echo -n "Downloading ${LDBC_JSON_FILE}: "
    curl -LJO "${LDBC_BASE_URL}"
    if [ $? -ne 0 ] || [ $(cat ${LDBC_JSON_FILE} | grep "404: Not Found" | wc -l) -ne 0 ] 
    then
        echo "Failed downloading JSON file" ; exit 1
    else
        echo OK
    fi
fi

if [ -f ${LDBC_JSON_FILE} ]
then
    if [ ! -f ${FLICT_TRANSLATION} ]
    then
        echo Creating flict translation file
        ./split-ldb.py ${LDBC_JSON_FILE} > ${FLICT_TRANSLATION}
    fi
else
    echo "No JSON file present.... , that sucks"
    exit 2
fi

if [ ! -f ${FLICT_TRANSLATION} ]
then
    echo "failed creating ${FLICT_TRANSLATION}"
    exit 3
fi

./list-transl.py  > ${ALIAS_REPORT_MD}
if [ ! -f ${ALIAS_REPORT_MD} ]
then
    echo "failed creating ${ALIAS_REPORT_MD}"
    exit 3
fi

pandoc ${ALIAS_REPORT_MD} -o ${ALIAS_REPORT_PDF}
if [ ! -f ${ALIAS_REPORT_PDF} ]
then
    echo "failed creating ${ALIAS_REPORT_PDF}"
    exit 3
fi
