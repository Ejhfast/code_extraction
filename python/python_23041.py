# User keywords return no value if they contain continuable failures in Robot Framework 2.8.5
Test case 1
    ${x}=  Run keyword and continue on failure   My Keyword
    Log    ${x}
