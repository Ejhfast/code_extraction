# Change svn node properties with Python raises a SubversionException
txn = svn.repos.fs_begin_txn_for_commit(repos_ptr, headrev, SVN_COMMIT_USER, SVN_COMMIT_MESSAGE)
root = svn.fs.txn_root(txn)
