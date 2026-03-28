# talosctl-rpm
Automated RPM packaging for talosctl. Provides a Fedora Copr repository with daily builds tracking the latest Sidero Labs releases.

## Installation
To install `talosctl` from this repository:

1. Enable the Copr repository:
   ```bash
   sudo dnf copr enable berndserk/talosctl-rpm

2. Install the package
   ```bash
   sudo dnf install talosctl
