# Choosing Scripting lang
function utf8_length(str)
        return select(2, string.gsub(str, "[^\128-\193]", ""));
end
