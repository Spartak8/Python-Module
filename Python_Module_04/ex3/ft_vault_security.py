def secure_archive(filename: str, mode: int = 0, content: str = "") -> tuple[bool, str]:
    if mode == 0:
        try:
            with open(f"{filename}", "r") as file:
                text = file.read()
            return(True, text)
        except Exception as e:
            return(False, str(e))
        
    elif mode == 1:
        try:
            with open(f"{filename}", "w") as file:
                file.write(content)
            return(True, "Content successfully written to file")
        except Exception as e:
            return(False, str(e))
        

print("=== Cyber Archives Security ===")
print()
print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file"))
print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("/etc/shadow"))
print("Using 'secure_archive' to read from a regular file:")
result = secure_archive("ancient_fragment.txt")
print(result)
print("Using 'secure_archive' to write previous content to a new file:")
print(secure_archive("new_fragment.txt", 1, result[1]))
