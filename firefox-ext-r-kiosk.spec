Summary:	Kiosk mode extension for Firefox
Name:		firefox-ext-r-kiosk
Version:	0.9.0
Release:	2
License:	GPLv2+
Group:		Networking/WWW
Url:		https://addons.mozilla.org/en-US/firefox/addon/r-kiosk
Source0:	https://addons.mozilla.org/firefox/downloads/file/132044/r_kiosk-0.9.0-fx.xpi
Buildarch:	noarch

BuildRequires:	firefox-devel
Requires:	firefox >= %{firefox_version}

%description
Kiosk mode extension for Firefox

%prep
%setup -qc

%install
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
	hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
	echo "Failed to find plugin hash."
	exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%files
%{firefox_extdir}/*
