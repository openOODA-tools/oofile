Name:           oofile
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign MIME detector, magic byte identifier, and encoding inspector
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/oofile
Source0:        oofile-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofile is a sovereign, capability-bounded MIME DETECTOR written
in pure openOODA, featuring zero ambient authority, magic-byte inspection,
MIME type resolution, text encoding detection, and a streaming Model Context Protocol (MCP) server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofile
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofile-uninstall

%files
/usr/bin/oofile
/usr/bin/oofile-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to sovereign pure openOODA v0.2.0 with magic bytes, MIME detection, and streaming MCP
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
