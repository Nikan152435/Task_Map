from error_repository.error_repository import ErrorRepository

repo = ErrorRepository()
repo.add_error(1, "Access denied")
print(repo.translate(1))  # Output: "Access denied"