def bump_version(version, part):
    parts = version.split('.')
    if part == 'major':
        parts[0] = str(int(parts[0]) + 1)
        parts[1] = '0'
        parts[2] = '0'
    elif part == 'minor':
        parts[1] = str(int(parts[1]) + 1)
        parts[2] = '0'
    elif part == 'patch':
        parts[2] = str(int(parts[2]) + 1)
    return '.'.join(parts)

if __name__ == "__main__":
    with open("VERSION", "r") as f:
        version = f.read().strip()
    
    version = bump_version(version, "patch")
    
    with open("VERSION", "w") as f:
        f.write(version)