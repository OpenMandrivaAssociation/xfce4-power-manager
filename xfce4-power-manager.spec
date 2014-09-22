%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	1.3.2
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/%{url_ver}/%{name}-%{version}.tar.bz2
# (tpg) https://bugzilla.xfce.org/show_bug.cgi?id=9963
Patch0:		xfce4-power-manager-1.2.0-add-systemd-logind-support.patch
BuildRequires:	pkgconfig(libxfconf-0) >= 4.10.0
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxfce4panel-1.0) >= 4.11
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
Requires:	pm-utils
Requires:	hibernate
Requires:	suspend-s2ram
Conflicts:	mandriva-xfce-config-common < 2009.1-2
Requires(pre):	xfconf
Requires:	upower

%description
A power manager dedicated for Xfce desktop environment.

%prep
%setup -q
%apply_patches

%build
#needed for patch 0
NOCONFIGURE=1 xdt-autogen

%configure2_5x \
	--enable-dpms \
	--enable-panel-plugins \
	--enable-network-manager \
	--enable-polkit

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sbindir}/xfpm-power-backlight-helper
%{_bindir}/%{name}*
%{_bindir}/xfce4-power-information
%{_libdir}/xfce4/panel-plugins/xfce4-brightness-plugin
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_datadir}/applications/*.desktop
%{_datadir}/xfce4/doc/C/images/*.png
%{_datadir}/xfce4/doc/C/xfce4-power-manager.html
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*
