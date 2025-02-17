import datetime

ORDER_DESCRIPTION = "ORDIN"
ORDER_NUMBER_REGEX = "ORDIN[^0-9]*([\d]+[^0-9]*)"
DOSSIER_REGEX = "\(([\d]+)\/[^0-9]*([\d]+)\)"
DOSSIER_REGEX_NO_PARENTHESES = "([\d]+)\/[^0-9]*([\d]+)"

DOSSIER_YEAR_MINIMUM = 2000
DOSSIER_YEAR_MAXIMUM = datetime.datetime.now().year
