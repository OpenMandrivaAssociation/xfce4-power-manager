%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	1.0.10
Release:	%mkrel 2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfconf-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4-panel-devel
BuildRequires:	polkit-1-devel
BuildRequires:	libxfce4ui-devel
Requires:	pm-utils
Requires:	hibernate
Requires:	suspend-s2ram
Requires:	devicekit-power
Conflicts:	mandriva-xfce-config-common < 2009.1-2
Requires(pre):	xfconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
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
