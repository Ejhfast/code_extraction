# scripting language to remove license preamble on files
perl -ne 'if (/#region/../#endregion/) {print if /#(?:end)?region/;next};print' file
