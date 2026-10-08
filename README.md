# oofile: Sovereign File Format & MIME Identifier

<div align="center">

```
================================================================================
                                oofile
               Sovereign openOODA File & MIME Identifier
================================================================================
```

**Sovereign File & MIME Detector**  
*Magic-byte based file format, MIME type, and encoding identification without exec or ambient authority.*  
*Two Faces, One Engine:* Modern POSIX terminal ergonomics • Streaming JSON-RPC 2.0 MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()
[![Release: v0.2.0](https://img.shields.io/badge/Release-v0.2.0-blue.svg)](https://github.com/openOODA-tools/oofile/releases/tag/v0.2.0)

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oofile/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oofile-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oofile/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oofile/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oofile-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oofile/uninstall.sh | bash -s -- --uninstall
```

---

## 2. CLI Usage

```
usage: oofile [options] [FILE...]

Magic-byte based file format, MIME type, and encoding identification without exec.

POSIX Options:
  -b, --brief           do not prepend filenames to output lines
  -i, --mime            output MIME type strings (--mime-type and --mime-encoding)
      --mime-type       output only the MIME type string
      --mime-encoding   output only the MIME encoding string
  -L, --dereference     follow symlinks
  -h, --no-dereference  do not follow symlinks [default]
  -j, --json            output file identification records as JSON Lines
  -D, --demo            synthetic multi-format file identification showcase
      --test            execute internal subsystem verification suite
      --mcp             run as Model Context Protocol JSON-RPC stdio server
  -v, --version         output version information and exit
      --help            display this help and exit
```

### Examples
```bash
# Standard identification
oofile main.oo dist/oofile
# main.oo: ASCII text
# dist/oofile: ELF 64-bit LSB executable, x86-64, version 1 (SYSV)

# Brief mode
oofile -b archive.zip
# Zip archive data

# MIME type and encoding
oofile -i document.pdf
# document.pdf: application/pdf; charset=binary

# Structured JSON output
oofile -j main.oo
# {
#   "path": "main.oo",
#   "mime_type": "text/plain",
#   "charset": "us-ascii",
#   "category": "text",
#   "description": "ASCII text",
#   "size": 3634
# }
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oofile` runs a JSON-RPC 2.0 stdio server providing streaming structured tools for AI coding agents:

```bash
oofile --mcp
```

### Registered Tools
| Tool Name | Parameters | Description |
|---|---|---|
| `file_identify` | `path` (string), `brief` (bool), `mime` (bool) | Identifies file format, MIME type, and encoding for target path |
| `file_mime_type` | `path` (string) | Returns only the MIME type string for target file |
| `file_detect_bytes` | `bytes` (string), `json_mode` (bool) | Detects format directly from in-memory string prefix bytes without disk I/O |
| `file_inspect_magic` | *(none)* | Lists recognized binary magic signatures, offsets, and MIME types |
| `file_demo` | *(none)* | Runs interactive multi-format file identification showcase |

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk or network leakage.
* **Negative-Trust Architecture:** Strict input bounds checking, zero dynamic evaluation or subprocess exec (`execve` banned).
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
