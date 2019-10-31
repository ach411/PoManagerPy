#!/bin/bash
# Utility script for developper to upgrade their local test dev database
# ACH, Oct 2019

set -euo pipefail
IFS=$'\n\t'

SQL_FILE="${1:-}"
DATABASE_NAME="po_manager_test"
USER="pomanager_tester"
PASS="123456"

display_usage()
{
    echo -e "Usage: \t${0} <file.sql>"
    #echo "Replace content of local dev database 'po_manager_test' by content of <file.sql> passed in arg"
    echo "Replace content of local dev database '${DATABASE_NAME}' by content of <file.sql> passed in arg"
    echo "<file.sql> must have been created by: mysqldump > file.sql"
    echo "DO NOT USE mysqldump --all-databases or --databases options to create file.sql"
    echo
}

check_arg_exists()
{
	if [ -z "${SQL_FILE}" ] ; then
		echo "argument <file.sql> is missing..."
		display_usage
		exit 1
	fi
}

check_sql_file_exists()
{
    if [ ! -e "./${SQL_FILE}" ]
    then
        echo "Could not find file ${SQL_FILE}..."
        exit -1
    fi
}

replace_database()
{
    mysql -u ${USER} -p${PASS} ${DATABASE_NAME} < ${SQL_FILE}
}

fix_revision_table()
{
    SQL_COMMAND="USE po_manager_test;"
    SQL_COMMAND="${SQL_COMMAND} UPDATE Revision SET revisionCust = null WHERE revisionCust = 'unknown';"
    SQL_COMMAND="${SQL_COMMAND} UPDATE Revision SET revision = null WHERE revision = 'unknown';"

    echo ${SQL_COMMAND} | mysql -u ${USER} -p${PASS}
}

main() {

    check_arg_exists

    check_sql_file_exists

    replace_database

    fix_revision_table

    echo "done"

}

main "$@"
