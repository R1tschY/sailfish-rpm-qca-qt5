Name:       qca-qt5-static
Summary:    Straightforward and cross-platform crypto API, using Qt datatypes and conventions.
Version:    2.2.1
Release:    1
License:    LGPLv2.1+
URL:        https://userbase.kde.org/QCA
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  extra-cmake-modules >= 5.68.0

%description
Straightforward and cross-platform crypto API, using Qt datatypes and conventions.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
mkdir -p build
cd build

cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_TESTS=OFF \
    -DBUILD_TOOLS=OFF \
    -DBUILD_PLUGINS=ossl \
    -DBUILD_SHARED_LIBS=OFF \
    ..
    
%make_build

%install
cd build
make install DESTDIR=%{buildroot}

%clean
rm -rf build

%files
%defattr(-,root,root,-)
%license COPYING

%{_includedir}/Qca-qt5/QtCrypto/*
%{_libdir}/cmake/Qca-qt5/*.cmake
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_libdir}/libqca-qt5.a
%{_libdir}/qca-qt5/crypto/libqca-ossl.a
%{_datadir}/man/man1/qcatool-qt5.1.gz
/usr/mkspecs/features/crypto.prf
