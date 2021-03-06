Summary:	A font viewer utility for GNOME
Name:		gnome-font-viewer
Version:	3.14.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-font-viewer/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	0f1253fbe57027478f895eba819db38d
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A font viewer utility for GNOME.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-font-viewer
%attr(755,root,root) %{_bindir}/gnome-thumbnail-font
%{_desktopdir}/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer

