%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	1.2.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfconf-devel >= 4.10.0
BuildRequires:	dbus-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:	libxfce4-panel-devel >= 4.10.0
BuildRequires:	polkit-1-devel
BuildRequires:	libxfce4ui-devel >= 4.10.0
Requires:	pm-utils
Requires:	hibernate
Requires:	suspend-s2ram
Requires:	upower
Conflicts:	mandriva-xfce-config-common < 2009.1-2
Requires(pre):	xfconf

%description
A power manager dedicated for Xfce desktop environment.

%prep
%setup -q

%build
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
