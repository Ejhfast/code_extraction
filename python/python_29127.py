# Django return file as string, not as a file
function download(path,val) {
    window.location.href = path+"download.php?val="+val;
};
