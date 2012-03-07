Name:		libopensync-plugin-akonadi
Version:	0.22
Release:	%mkrel 1
Summary:	KDE4 Akonadi PIM Synchronization Plug-In for OpenSync
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.opensync.org/wiki/plugins/akonadi
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libopensync-plugin-akonadi-kde4.4.patch
BuildRequires:	pkgconfig(opensync-1.0)
BuildRequires:	pkgconfig(osengine-1.0)
BuildRequires:	cmake
BuildRequires:	kdepim4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	libopensync >= %{version}

%description
This plug-in allows applications using OpenSync to synchronize to and
from KDE4 Akonadi-based applications.

#-------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/opensync/plugins/akonadi_synclib.so
%{_libdir}/opensync/plugins/akonadi_sync.so
%{_datadir}/opensync/defaults/akonadi-sync



