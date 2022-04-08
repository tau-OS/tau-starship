%define adw_version 1.6

Summary:        tauOS Configuration for Starship
Name:           tau-starship
Version:        1.1
Release:        1
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       starship

%description
tauOS Configuration for the Starship shell

%prep
%setup -q
%build

%install
# Install the starship config
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -Dm0644 starship.toml -t %{buildroot}%{_sysconfdir}/
install -Dm0644 starship.sh -t %{buildroot}%{_sysconfdir}/profile.d

# Install licenses
mkdir -p licenses
install -pm 0644 LICENSE licenses/LICENSE

%files
%license licenses/LICENSE
%config(noreplace) %{_sysconfdir}/starship.toml
%config(noreplace) %{_sysconfdir}/profile.d/starship.sh

%changelog
* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release