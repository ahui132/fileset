# fileset
This is a shell tool which used to calculate the line set of two file.

# Usage

        fileset [OPTIONS] FILE1 {SET_OPERATOR} FILE2

        SET_OPERATOR
            +   Union set
            -   Difference set
            -i  Intersection set
        OPTION
            -h  For help
            -d <delimiter>
                Set delimiter( `,` is default delimiter)
            -f n
                Compare the n'th field(The default is whole line)

# Example

        fileset a + b
            Union set of a and b.
        fileset a -  b
            Difference set: a minus b
        fileset a -i b
            Intersection set of a and b.

		$ cat a
		111
		222
		333

		$ cat b
		222
		333

		$ fileset a - b
		111


