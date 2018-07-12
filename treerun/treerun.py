#!/usr/bin/env python

########################################################################################################################

#
# treerun.py  v0.9
# ---------------------
#
#    Traverse a directory tree recursively. Use a callback.
#
# Author: Jimmy Gizmo
# Organization: Ninth Device
# http://ninthdevice.com
# Version: 0.9
# Version date: 2018-06-25
# Created: 2015-07-28
#
# Developed under Python 2.7.9. Should work with recent 2.7.* versions. Only standard/core modules are used.
# Non-core modules may be referenced, but only in commented-out helper code as potentially-useful recommendations.
#

########################################################################################################################

#
# License: MIT.
# The MIT license is one of the most open, permissive and simple Open Source licenses. See LICENSE.txt at this URL:
# GitHub repository: https://github.com/jimmygizmo/zerotools
#
#
# The MIT License (MIT)
#
# Copyright (c) 2018 Jimmy Gizmo, Ninth Device
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

########################################################################################################################

#
# #### FEATURES IN VERSION 0.9 ####
#
# This python application template is designed to be a solid starting point for almost any kind of application, be it a
# command-line utility, client, server or GUI application. The following features are provided:
#
# Only standard/core modules present in Python 2.7.9 are used, so no module installation is necessary.
#
# Full-featured POSIX command-line argument processing with a few basic initial commands implemented to control the
# logging verbosity level and other such facilities useful to almost any kind of application. In this template, I've
# shown how to do the configuration of the argparse module. The argparse module is powerful and has a lot of options,
# so there are some nuances to using it effectively. This template shows you an effective way to use argparse.
#
# Object-oriented python with a clean class structure intended as a solid-foundation to build a best-practice OO python
# application from. A Base class which is never instantiated provides global logging and configuration. An App class
# then adds the command-line processing and run() method as the starting point to take user input and then dispatch
# the specific operations the user is requesting.
#
# Powerful, industry-standard logging, implemented on a very simple and usable level. If your application grows into
# something big and complex, then you can move into the more advanced capabilities of the logging module. However,
# even the simplest of applications should have robust logging. The benefits are huge. Appbootstrap has a very good
# basic logging system in place out of the box. You can go a long way with the single --verbose switch to control
# just INFO and DEBUG logging levels. You should include DEBUG logging calls everywhere and take full advantage
# of the debugging, transparency, optimization, monitoring, audit and other benefits of rich DEBUG logging. Choose
# to make INFO vs. DEBUG logging calls based on the activity-level of your app, disk-space or your personal taste.
#
# Easy-to-find and easy-to-edit in-code configuration through the use of a namespace-only "config" class in main.
# This hack works well as a way to have infrequently-changing global configuration information directly in your code.
# Since configuration-in-code will not suit all needs, an upcoming version of appbootstrap is going to offer a clean
# and simple file-based configuration strategy which will be handled all in the Base class. This will further minimize
# the amount of stuff we are doing in __main__ and of course offer separation of code from configuration.
#
# Care has been taken to follow best practices in as many areas as possible. Best-practices known in the Python
# community as well as best practices learned from nearly 20 years writing code and building infrastructure for the
# industry's top companies.
#
# The is both a running template and coding starting point but it is also a teaching tool. Generous comments,
# doc strings, informative example text, clear yet concise object names; all contribute to assist the developer in
# learning key concepts and solving basic problems in a practical way so that good apps can be created quickly and
# built upon with a good understanding of how best to use Python.
#
# Planned enhancement path. Subsequent version are planned to take many good concepts further and add valuable
# functionality. At some point, appbootstrap may divide into a few different types, intended for different kinds
# of applications. This author is always learning, just like you are, so as improvements become evident, they will
# be incorporated while continuing to keep things simple, practical, effective and powerful. Not every bell and
# whistle will be included. Many details and complexities will be left out if they are not truly valuable.
#

########################################################################################################################

#
# PEP8 Coding-Style Recommendations
#
# The code in this application template closely follows the PEP8 recommendations and is regularly validated with the
# PEP8 tool during development. Some examples are: Line width of 120 characters. Alignment of multi-element lists and
# other entities which span multiple lines for improved readability. 4 spaces for each indentation level. Thorough use
# of doc strings and much more. Other coding and commenting styles are used to include as much helpful information and
# structure as possible in this template.
#

###############################################  PYTHON CORE LIBRARIES  ################################################


import logging
import argparse
import time
import os
import sys

# Other essential core modules you may want to use early in your new application:
# import io
# import re


############################################  3RD-PARTY (SITE) LIBRARIES  ##############################################


# If you want to expand beyond Python's standard core modules and install other very powerful modules into your
# environment, then have a look at the power of some of these for all kinds of development needs:
# import requests
# import pexpect
# import dicttoxml


############################################  GLOBAL CONFIGURATION SETTINGS  ###########################################


class config:
    """This config class is used as a global namespace only. No instances are created. There are no methods. Used as a
    convenient way to access global, infrequently-changing configuration information. The lowercase name of config
    is intentional here. This is not a regular class, so its name is not capitalized like a regular class. The config
    values specified just below here are being set from __main__ and should be kept here near the top of the code.
    This class definition actually ends immediately here with 'pass' since all we want to do is create the namespace."""
    pass
    # This might be considered a hack, but it is a clean hack which works well for in-code configuration like this.

config.app_nick = "treerun"  # Application Nickname. This will be used to name logfiles and more so it should
# consist only of lower-case letters, numbers or underscore.

config.log_filename = config.app_nick + ".log"

# Directory where log files should be created.
config.log_path = "."  # . is current directory

# Fields and format for the log lines. Refer to the documentation for the 'logging' module.
config.log_format = '%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)s %(message)s'

config.log_file = config.log_path + "/" + config.log_filename

# The default logging level to be used initially, prior to any adjustments made via command-line options:
config.default_log_level = logging.INFO
# Although there are many logging levels available in the logging module, we are keeping this application template
# simple and will only use two: INFO and DEBUG, controlled with a single --verbose option. Feel free to call any
# of the log actions. You will see WARN, ERROR and CRITICAL messages in either INFO or DEBUG log_levels. We have not
# limited the message types/levels. We have only limited the selection of log level to a single --verbose switch.


#################################################  CLASS DEFINITIONS  ##################################################


class Base(object):
    """The 'Base' class is literally the base class of this application, the main purpose of which is to provide
    convenient access to logging and configuration. As you develop your application, other facilities and data at this
    base-level may be added to this class. Briefly, let's recall that there is the __main__ or global scope which
    is sort of a base to all classes in python. So in one sense, __main__ is a base of Base but in OO terms, Base is
    our base CLASS. Appbootstrap intends to follow best practices in OOP as well as in many other areas, so we
    want to have a minimum of objects (variables and functions etc.) in the global/main space. We should maintain a
    tendency to try to move anything in main to Base if possible, but not to an unreasonable degree.
    A bit more about main; Some things are very convenient to have in the main/global space, such as the config
    namespace we use as a clear, self-documenting place to edit infrequently-changing configuration information in
    appbootstrap. In future versions of the appbootstrap template, config might be handled in some other way, perhaps
    through loading a config file, entirely in the Base class and not involving the main namespace, but having config
    as a simple namespace in main near the top of the code is clean and convenient for now.
    Base should be inherited by all classes in appbootstrap unless the class is so simple that it does not need
    access to logging or configuration data but since it is a good idea to have a LOT of ability to log information
    especially at the verbose/DEBUG level, then I can say that really ALL classes should inherit from Base or from
    another class which is a subclass of Base."""

    def __init__(self, config, logger):
        """Base is never instantiated. It is always inherited. However, this constructor is definitely used. Classes
        which inherit from Base will in most cases use python's super() call to invoke Base.__init__() in order to
        initialize config, logger and other objects into their own namespace(s). This will be done from within the
        __init__ of the sub-class. See App.__init__() for an example."""
        self.cfg = config
        self.log = logger

        # This log line is here for illustrative purposes and is only active if you change config.default_log_level
        # to DEBUG in the code. Command-line options have not been processed yet so --verbose cannot take effect yet.
        self.log.debug("Base class __init__ executed.")


class App(Base):
    """The App class is the central point of activity for this application. There should be only one instance of the App
    class and it is during the __init__ of this class when all processing of command-line arguments is done by calling
    the process_cmd_line() method. This is the application-specific processing during which you will validate the
    sanity of all supplied options and values and where you will provide thorough feedback to the user in case they
    have supplied any invalid options. The App class contains the application's run() method which is the point from
    which you should dispatch the highest level program operations. For example, if your program is a command-line
    utility and handles 4 commands, then within App.run() you should detect the specific command and then
    dispatch/execute operations for that command. App inherits from Base, which provides convenient access to logging,
    configuration and possibly other facilities needed by App or other classes."""

    def __init__(self, config, logger, cmd_line_parser):
        """Constructor for App objects, of which there is currently only intended to be one instance. Command-line
        options are processed here by calling the method for that purpose, during which time related feedback or errors
        are thoroughly communicated to the user. Most initialization, sanity-checking and pre-dispatch user feedback
        should occur process_cmd_line() or some other method which is always called by this __init__."""

        # App inherits from Base. No instance of Base is ever created, so we call the __init__ of Base like this
        # and thereby get the attributes from the __init__ of Base initialized here into App.
        super(App, self).__init__(config, logger)
        # self.cfg, inherited from Base, has now been initialized.
        # self.log, inherited from Base, has now been initialized.
        self.tree = None
        self.depth = -1  # Prior to starting traversal, such that root node is depth 0. TODO: Verify this convention.
        # TODO: Implement depth. Currently lacking the method to calculate depth.
        self.node_count = 0  # TODO: Possibly move this to a static/class attribute of the Node class.

        self.arg = cmd_line_parser.parse_args()  # A namespace object is returned to self.arg here. See argparse docs.

        # This log line is here for illustrative purposes and is only active if you change config.default_log_level
        # to DEBUG in the code. Command-line options have not been processed yet so --verbose cannot take effect yet.
        self.log.debug("App class instantiated. Command-line options will now be processed.")

        self.process_cmd_line()

    def process_cmd_line(self):  # The term "command-line options" is interchangeable with "command-line arguments"
        if self.arg.verbose:  # See how we use the exact name of the option to access it. These can be different types.
            self.log.setLevel(logging.DEBUG)
            self.log.debug("Verbose mode is now active. Log level set to DEBUG.")
        else:
            self.log.info("Using default log level of " + logging.getLevelName(self.cfg.default_log_level))


    def run(self):
        self.log.info("Application " + self.cfg.app_nick + " is now running.")

        abs_path = os.path.abspath(self.arg.path)
        self.log.debug("os.path.abspath of path is: " + str(abs_path))

        if not os.path.isdir(abs_path):
            self.log.error("The --path value does not represent a valid directory in the filesystem.")
            sys.exit(1)

        #self.tree = Node(path=abspath, name="Root", type="dir")

        self.log.debug("Beginning traversal of the filesystem tree at the root path provided.")

        # Initialize the tree with the root node.
        # The filesystem will be traversed recursively, with the full hierarchy of child nodes being added to the root.
        # The tree is the root node and all of its child nodes, so a Node object (which IS the tree) will be returned.
        # TODO: Combine redundant following comment with above. Rewrite above.:
        # Initialize the tree by creating an instance of Node for the root of the filesystem at our path.
        root_node = Node(path=abs_path, name="Root Node", node_type="dir", attributes=None)

        # Complete the tree by recursively processing the root node to add all child nodes, returning the full tree.
        self.tree = self.process_dir(root_node)

    def process_dir(self, current_node):
        Node.current_traversal_depth += 1  # Class attribute. # TODO: Should we access it like this here?
        # TODO: OR .. we could make a class method to: increase_current_traversal_depth()
        # TODO: Similarly: decrease_depth() get_max_depth()
        self.node_count += 1  # A variable in the App class, parallel to Node.count
        # Note that the class attribute Node.count should also increment automatically.
        # Node.count should also be accessible through any instance as node_instance.count/self.count etc.
        # TODO: Probably will just go with Node.count. Then deprecate App's self.node_count.
        type = None

        self.log.debug("- - Processing directory at path of current node: " + str(current_node.path))

        # Recursive processing
        for dir_item in os.listdir(current_node.path):
            dir_item.rstrip()  # On Windows and possibly all OSes, trailing newline must be stripped.
            # TODO: Test on Linux and OSX as well to determine if os.listdir returns trailing newlines on them as well.
            path_dir_item = os.path.join(current_node.path, dir_item)
            #abs_path_dir_item = os.path.abspath(dir_item)  # Not necessary. We just composed the absolute path.
            abs_path_dir_item = path_dir_item
            self.log.debug("- - - - ## Creating new Node.")
            self.log.debug("- - - - Path of current dir_item is: " + str(abs_path_dir_item))
            self.log.debug("- - - - New Node name: " + str(dir_item))

            if os.path.isdir(abs_path_dir_item):
                node_type = 'dir'
                self.log.debug("- - - - New Node is of type 'dir'")
                new_child_node = Node(path=abs_path_dir_item, name=dir_item, node_type="dir", attributes=None)
                current_node.add_child(new_child_node)
                self.log.debug("- - - - Node count: " + str(Node.count))
                # RECURSE FURTHER
                self.process_dir(new_child_node)
            else:
                node_type = 'file'
                self.log.debug("- - - - New Node is of type 'file'")
                new_file_node = Node(path=abs_path_dir_item, name=dir_item, node_type="file", attributes="coming soon")
                current_node.add_file(new_file_node)
                self.log.debug("- - - - Node count: " + str(Node.count))
                # Files are just added to their current node with no recursion involved.

        self.log.debug("- - Completed processing directory: " + current_node.path)

        return current_node


class Node(object):
    """Node objects make up the data of the tree structure. Instances of Node are linked to each other via the 'children'
    attribute which is of type list, the elements of which are themselves Node objects. A Node can be of type 'file'
    or type 'dir'. Only Nodes of type 'dir' can have any children. Nodes of type file have more attributes than nodes
    of type 'dir'."""
    # Class attributes:
    count = 0
    current_traversal_depth = -1  # -1 means traversal has not yet begun. root node is depth 0.
    max_traversal_depth = -1  # max will parallel current upwards in value during traversal and then stay at max

    def __init__(self, path, name, node_type, attributes):
        self.__class__.count += 1
        self.path = path
        self.name = name
        self.node_type = node_type  # "dir", "file"
        # TODO: Consider adding a "root" type which would be a special kind of dir type for the root node.
        self.attributes = attributes # file attributes for Nodes of type 'file'
        self.children = []  # list of child Node objects for Nodes of type 'dir'
        self.files = []  # list of contained Node objects for Nodes of type 'file'

        # TODO: We should generate/carry attributes for directories as well. Why not?

    def add_child(self, child):
        if not self.node_type == "dir":
            print "Adding child Node failed. Current node is not of type 'dir'. Only dir Nodes can contain child " \
            "dir Nodes."
            return  # Not currently a fatal error. TODO: How to handle exceptions since we don't want logging in here.
        else:
            self.children.append(child)

    def add_file(self, file):
        if not self.node_type == "dir":
            print "Adding file Node failed. Current node is not of type 'dir'. Only dir Nodes can contain file."
            return  # Not currently a fatal error. TODO: How to handle exceptions since we don't want logging in here.
        else:
            self.children.append(file)

    def child_count(self):
        return len(self.children)

    def file_count(self):
        return len(self.files)


########################################################  MAIN  ########################################################


def main():
    """The starting point for program execution. main() is not called if this file is imported as a python module.
    main() exits with an integer process exit status of 0 for success and a non-zero integer for any error condition.
    Specific non-zero values will depend on your application, your environment and how you choose to implement such
    conventions, perform error trapping, etc. 0 for success is mandatory. Non-zero values are up to you. main()
    initializes the global logger and starts this application with App.run(). When the program is almost done operating,
    the last part of main() can then perform any finalization and cleanup prior to exit. This application does not
    currently support importing as a module, although it could with some minimal changes."""

    root_logger_name = config.app_nick + "-main"

    logging.basicConfig(filename=config.log_file,
                        format=config.log_format,
                        level=config.default_log_level)

    logger = logging.getLogger(root_logger_name)

    start_time_machine = time.time()
    start_time_human = time.asctime(time.localtime(start_time_machine))
    logger.info("")  # We append to an existing log file, so a blank line and dashes make the startup more visible.
    logger.info("- - - - - - - - - - Initializing " + config.app_nick + " " + start_time_human)
    logger.info("Instantiated root logger: " + root_logger_name)

    app = App(config, logger, cmd_line_parser)
    app.run()

    return 0


################################################  MAIN EXECUTION BEGINS  ###############################################


#### ARGPARSE COMMAND-LINE OPTIONS AND HELP CONFIGURATION ####

#
# The argparse module is configured below. Replace all of the instructional template text with your own description,
# instructions, commands and options below. There is a ton of information on how best to use argparse embodied in the
# below template code. Have a close look at it and try it out. Read up on the argparse module .. it is your friend and
# it is a python core module which can benefit nearly all python programs. It just takes a little finesse to really use
# it to its full potential.
#
# An 80-character ruler is provided below and the instructional text discusses in detail that you can choose to use
# either full-width-wrapping text or fixed-formatting and therefore fixed-width text for doing things like indenting
# or inserting blank-lines or avoiding the need to escape apostrophes, quotes, newlines or other characters.
# The important point to make here, is that IF you use fixed-formatting .. DON'T exceed 80 characters in width,
# because many console windows might be open at this typical default width. Also, most unix and linux commands have
# their help-text limited to 80 characters. What you should not do is use fixed-formatting over 80 characters, because
# although this is not going to break anything, it means you will end up with a bunch of lines with only one or a few
# words on them in-between the longer lines. Ugly as heck. If you want longer lines, just use the wrapping style.
# I show you how to intermix both styles easily below. Argparse documentation does not go into this level of detail.
#
# One more important point; this formatting technique is dependent upon using the argparse option:
# formatter_class=argparse.RawDescriptionHelpFormatter
#
# See below and see the documentation for the argparse module for more information.
#

################################################################################
# These bars are 80 characters wide, useful for fixed-formatting in argparse.
# Read below about full-width-wrapping vs. fixed-formatting limited to 80 chars.
################################################################################

cmd_line_parser = argparse.ArgumentParser(
    description="""This is the program description shown when the --help or -h command-line options are invoked."""
                """Notice how triple-double quotes are used here and also notice how the first part of this """
                """description has opening and closing quotes on each line with included space characters after """
                """the last word on each line. The lower part of this description needs to use fixed-formatting """
                """because we are using indentation and blank lines to highlight some important commands for our """
                """program. It is this fixed-formatting part at the end which requires us to use triple-double """
                """quotes in this manner for the entire description. Since we don't need the fixed-formatting """
                """for the first part of the description and we do want the lines to wrap, that is why we also have """
                """closing quotes up here. In the lower part, we must continue using the same kind of quotes """
                """because this entire description is a single attribute and we cannot mix quote types here. """
                """If you do not need any fancy fixed-formatting in your description then you can simplify the """
                """quoting, but helping the reader with formatting and thorough help text can be worth the """
                """effort. The triple quotes mean we do not have to escape apostrophes or newlines and it also """
                """means we can easily read and edit our own fixed formatting here in the code itself. So this part """
                """of the description text will wrap at the full console width where it is displayed, but the below """
                """fixed-formatting part we will hard-wrap at no more than 80 characters. The PEP8 coding standards """
                """being followed in this python code means our code line width is no more than 120 characters, but """
                """the maximum width of fixed-formatted help text should not exceed 80 characters and this is the """
                """standard you will see in most if not all unix/linux command help displayed in a console.

            Now we are in the section which drives the use of the triple-quotes.
            Note that an 80-character-line ends -------------here------------->|
            This fixed-format section stays within 80 characters in width and we
            are also indenting because this is a special section, now more for
            instructions, rather than the general description we did above with
            the wrapping-lines which will go the full width of any console.
            We have a blank line and indentation included already before this
            section and the indentation makes this special paragraph stand out
            because we are highlighting an important aspect of using this
            program. This information is a little different from the general
            program description which goes above and which should wrap lines.

            This section here could also wrap lines and if we wanted to do
            that then we would just have continued to use closing quotes with
            needed space characters at the end down to this point. You do not
            have to format things like this, but careful formatting can really
            help users get to important information faster. While this paragraph
            could have used wrapping, the part below here cannot as we must have
            the fixed formatting to have the indentation and blank lines needed
            to clearly document the commands we list below.

            Your program does not need to have a --command option or even help
            text which is this complex. The idea of a --command option which
            supports many different commands is just a good example of something
            which is best documented in this manner. Using the help attribute of
            individual argparse add_option items does not allow you to
            communicate this information as clearly as you can in the
            description with the method I have shown here. And now even more
            formatting of a very fixed nature, for example:

            Commands (via --command):

                load = Load all widgets and harvest widget data.

                convert = Convert all loaded widgets and data into doo-dads.

                save = Save all doo-dads.

                dump = Serialize all widgets into separate xml files.
            """,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    add_help=True)

cmd_line_parser.add_argument(
    '--verbose',
    action='store_true',
    help='Include a high level of detail in the log and in any output to the user. This option changes the log level'
         ' from INFO to DEBUG. The specific types of information which will be added and whether it is added just to'
         ' the log or also to user output will depend on the application. Customize this text to your application.')

cmd_line_parser.add_argument(
    '--path',
    action='store',
    help='Path at which to begin the traversal of the filesystem. This must be a directory. This requirement could be'
         ' lifted if this program would process any node, file or directory, even a single file as the root. It is'
         ' an arbitrary convention to require this as a directory, applied because the focus of this app is traversal.'
         ' String representing a valid path to a directory on the current filesystem.')

# Command-line parsing has now been configured and we can start initializing and then running the application.

status = main()  # Start program execution.
exit(status)  # Program execution ends, returning the integer returned by main to the shell as the process exit status.


##
#
