import qbs;

Project {
    name: "NameIt";

    Product {
        name: "nameit";
        type: "staticlibrary";
        targetName: "nameit";

        Export {
            Depends { name: "cpp"; }
            cpp.includePaths: ".";
        }

        Group {
            name: "C++ headers";
            files: [
                "nameit.h",
            ]
        }
    }
}
