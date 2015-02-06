%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	1.4.2
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfconf-0) >= 4.10.0
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxfce4panel-1.0) >= 4.11
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
Requires:	pm-utils
Requires:	hibernate
Conflicts:	mandriva-xfce-config-common < 2009.1-2
Requires(pre):	xfconf
Requires:	upower

%description
A power manager dedicated for Xfce desktop environment.

%prep
%setup -q
%apply_patches

%build
%configure \
	--with-backend=linux \
	--enable-panel-plugins \
	--enable-network-manager \
	--enable-polkit \
	--enable-xfce4panel

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sbindir}/xfpm-power-backlight-helper
%{_sbindir}/xfce4-pm-helper
%{_bindir}/%{name}*
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_datadir}/appdata/xfce4-power-manager.appdata.xml
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*
