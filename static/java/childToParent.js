function openTabInParent(url) {
    // Open the URL in a new tab of the parent window
    if (window.opener) {
        window.opener.open(url, '_blank');
    } else {
        alert('Parent window reference not found!');
    }
}