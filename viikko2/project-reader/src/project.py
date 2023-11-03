class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _list_dependencies(self, dependencies):
        return "\n".join([f"-{dependency}" for dependency in dependencies]) if len(dependencies) > 0 else "-"
    
    def _list_authors(self, authors):
        return "\n".join([f"-{author}" for author in authors]) if len(authors) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:\n{self._list_authors(self.authors)}"
            f"\n"
            f"\nDependencies:\n{self._list_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n{self._list_dependencies(self.dev_dependencies)}"
        )
