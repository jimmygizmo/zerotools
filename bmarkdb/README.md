###############################################################################
 
# FROM:
# https://www.npmjs.com/package/bookmarks-parser


Example:

 
var parse = require("bookmarks-parser");
parse('<title>Pocket Export</title><h1>Unread</h1>'+
      '<ul><li><a href="http://example.com">Example!</a></li></ul>', function(err, res) {
  console.log(err);
  console.log(res.parser);
  console.log(res.bookmarks);
});
 

parse function receives two parameters - text of a exported bookmarks file and callback.

Second parameter returned in the callback is an object with fields:

    parser - netscape or pocket
    bookmarks - an array of parsed bookmarks

Each bookmark is an object with fields:

    type - folder or bookmark
    title - title of a bookmark or a folder
    url - URL only for bookmarks
    children - array of children bookmarks, only for folders
    ns_root - if the folder is a root this field will contain one of the values: menu, toolbar, unsorted, otherwise null. Applicable only for netscape parser.


##
#

