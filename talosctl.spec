Name:           talosctl
Version: 1.13.4
Release: 1%{?dist}
Summary:        CLI for Talos Linux
License:        MPL-2.0
URL:            https://github.com/siderolabs/talos

# Build dependencies needed inside the Copr environment
BuildRequires:  curl
BuildRequires:  grep

%description
talosctl is the CLI tool for managing Talos Linux nodes and clusters.
This package is automatically updated daily via a GitHub Actions pipeline.

%prep
# No source to unpack, we download the binary in the build step

%build
# Detect architecture and set the correct binary suffix
%ifarch x86_64
    %global arch_suffix amd64
%endif
%ifarch aarch64
    %global arch_suffix arm64
%endif

# Download the binary for the correct architecture
curl -L https://github.com/siderolabs/talos/releases/download/v%{version}/talosctl-linux-%{arch_suffix} -o talosctl
chmod +x talosctl

%install
install -D -m 0755 talosctl %{buildroot}%{_bindir}/talosctl

%check
# This runs after installation but before the RPM is packaged
# 1. Check if the file exists in the buildroot
test -f %{buildroot}%{_bindir}/talosctl
# 2. Run the binary to ensure it reports the correct version
# We use --client to avoid it trying to connect to a real cluster
%{buildroot}%{_bindir}/talosctl version --client --short | grep "%{version}"

%files
%{_bindir}/talosctl

%changelog
* Sat Mar 28 2026 Bernd Putsche <bernd.putsche@gmail.com> - 1.12.6-1
- Initial automated build with multi-arch and check support
