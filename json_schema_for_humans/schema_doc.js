$(document).on('click', 'a[href^=#]', function(event) {
  event.preventDefault();
  history.pushState({}, '', this.href);
});

function setAnchor(anchorLinkDestination) {
    // Set anchor link without reloading
    history.pushState({}, '', anchorLinkDestination);
}

function anchorOnLoad() {
    // Added to onload on body, checks if there is an anchor link and if so, expan
    let linkTarget = window.location.hash.split("?")[0].split("&")[0];
    if (linkTarget[0] === "#") {
        linkTarget = linkTarget.substr(1);
    }

    if (linkTarget.length > 0) {
        anchorLink(linkTarget);
    }
}

function anchorLink(linkTarget) {
    const target = $( "#" + linkTarget );
    // Find the targeted element to expand and all its parents that can be expanded
    target.parents().addBack().filter(".collapse:not(.show), .tab-pane, [role='tab']").each(
        function(index) {
            if($( this ).hasClass("collapse")) {
                $( this ).collapse("show");
            } else if ($( this ).hasClass("tab-pane")) {
                // We have the pane and not the the tab itself, find the tab
                const tabToShow = $( "a[href='#" + $( this ).attr("id") + "']" );
                if (tabToShow) {
                    tabToShow.tab("show");
                }
            } else if ($( this ).attr("role") === "tab") {
                // The tab is not a parent of underlying elements, the tab pane is
                // However, it can still be linked directly
                $( this ).tab("show");
            }
        }
    );

    // Wait a little so the user has time to see the page scroll
    // Or maybe it is to be sure everything is expanded before scrolling and I was not able to bind to the bootstrap
    // events in a way that works all the time, we may never know
    setTimeout(function() {
        document.getElementById(linkTarget).scrollIntoView({ block: "center", behavior:"smooth" });
    }, 1000);
}