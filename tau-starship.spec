Summary:        tauOS Configuration for Starship
Name:           tau-starship
Version:        1.1
Release:        4
License:        GPLv3
URL:            https://tauos.co
Source0:        README.md
Source1:        LICENSE
Source2:        starship.sh
Source3:        starship.toml

BuildArch:      noarch

Requires:       starship

%description
tauOS Configuration for the Starship shell prompt

%prep

%build

%install
# Install the starship config
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -Dm0644 %SOURCE3 -t %{buildroot}%{_sysconfdir}/
install -Dm0644 %SOURCE2 -t %{buildroot}%{_sysconfdir}/profile.d

# Install licenses
mkdir -p licenses
install -pm 0644 %SOURCE1 licenses/LICENSE

install -pm 0644 %SOURCE0 README.md

%post
# Initialise starship automatically in RC files
if [ -f %{_sysconfdir}/skel/.bashrc ]; then
    echo 'eval "$(starship init bash)"' >> %{_sysconfdir}/skel/.bashrc
fi

if [ -f %{_sysconfdir}/skel/.zshrc ]; then
    echo 'eval "$(starship init zsh)"' >> %{_sysconfdir}/skel/.zshrc
fi

%files
%doc README.md
%license licenses/LICENSE
%config(noreplace) %{_sysconfdir}/starship.toml
%config(noreplace) %{_sysconfdir}/profile.d/starship.sh

%changelog
* Mon Jun 6 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1.3
- Only install init scripts if file exists

* Sat Apr 23 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1.2
- Update CI

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
