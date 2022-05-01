prtspool by Tim Pinkawa
http://www.timpinkawa.net/hercules

prtspool is a simple print spooler for use with MVS and JES2 running on Hercules.

*** Overview
prtspool uses the 1403 print to pipe functionality in Hercules. It captures the printer output and generates a text file for each job run. It can optionally run a command to process the text file afterwards.

*** Compiling
prtspool has been tested with gcc on Linux and will also compile with gcc on Windows. It is a simple program and should compile with any C compiler. To compile with gcc on Linux, use:
gcc -o prtspool prtspool.c

*** Usage
Modify your MVS configuration file to print to prtspool. For example, if you wanted to change PRINTER1 to use prtspool instead of a text file, replace:
000E 1403 prt00e.txt
with
000E 1403 "|prtspool A /path/to/output/ cmd"

This assumes that prtspool is in your path. If not, you must use a fully qualified path. (i.e. /usr/hercules/bin/prtspool)
The first parameter, A, tells prtspool to look for MSGCLASS=A output.

The second parameter is a path with a trailing slash which tells prtspool where to send the output. The files are named job-N.txt, where N is the job number starting at 1 and incremented after each job.

The third parameter is an optional parameter that will be called after each job is spooled. This allows the user to write a shell script or program to process each job as it is printed. For example, a shell script could be written which sends the output to a real printer. This command must also be in your path, otherwise a fully qualified path is required.

The command is passed the first and second parameter (MSGCLASS and directory) in that order. In this example, when cmd is called, it will be invoked as "cmd A /path/to/output/".

*** Example
A sample bash shell script, prtpdf, is included. This shell script will enumerate through the jobs in the output directory and convert them to landscape PDFs using enscript and Ghostscript.

*** Disclaimers and Warnings
prtspool has only been tested on the MVS Turnkey v3 system. It works by looking for four lines of "****{class}   END" at the end of every job. On some MVS systems, this line is only printed once and therefore it will not work. It is fairly simple to modify, though.

Every time prtspool is started (usually every IPL), the job counter is reset to 1 and any jobs in the output folder will be overwritten.

I am by no means an experienced C programmer. I have tried to use safe functions (snprintf, fgets) where possible. I don't believe there are any security issues with the code, but I can't guarantee it. prtspool runs as the user which runs Hercules, which may be a root or Administrator account. In general, the program assumes that you know what you're doing, for example, that you have write permission to where you're pointing the output and that the directory exists.
