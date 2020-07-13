Name:           saltunnel
Version:        0.0.1
Release:        1%{?dist}
Summary:        A simple, secure TCP tunnel.

License:        Public Domain
URL:            https://github.com/notfed/saltunnel
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
Requires:       libsodium-devel libsodium-static

%description
saltunnel is a cryptographically secure TCP tunnel. It allows one to augment a normally-insecure TCP session with state-of-the-art security, with minimal hassle and minimal impact on performance.

%prep
%autosetup

%build
./autogen.sh --prefix=%{_prefix} 

./configure
make

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -fr %{buildroot}

%files
/usr/local/bin/saltunnel
/usr/local/share/man/man1/saltunnel.1

%changelog
* Mon Jul 13 2020 Jay Sullivan <jay@identity.pub>
- saltunnel-0.0.1
