%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	4.20.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		https://goodies.xfce.org/projects/applications/%{name}
Source0:	https://archive.xfce.org/src/xfce/xfce4-power-manager/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	intltool
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  polkit-devel
Requires:	xfce4-panel
Conflicts:	mandriva-xfce-config-common < 2009.1-2
Requires(pre):	xfconf
Requires:	upower

%description
A power manager dedicated for Xfce desktop environment.

%prep
%autosetup -p1

%build
%configure \
	--with-backend=linux \
	--enable-panel-plugins \
	--enable-network-manager \
	--enable-polkit \
	--enable-xfce4panel

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS README*
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sbindir}/xfpm-power-backlight-helper
%{_sbindir}/xfce4-pm-helper
%{_bindir}/%{name}*
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_datadir}/metainfo/xfce4-power-manager.appdata.xml
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*
