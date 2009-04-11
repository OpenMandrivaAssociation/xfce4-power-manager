%define subrel beta1
Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	0.8.0
Release:	%mkrel -c %subrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://goodies.xfce.org/releases/xfce4-power-manager/%{name}-%{version}%{subrel}.tar.bz2
BuildRequires:	xfconf-devel
BuildRequires:	hal-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4-panel-devel
Requires:	pm-utils
Requires:	hibernate
Requires:	suspend-s2ram
Conflicts:	mandriva-xfce-config-common < 2009.1-2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A power manager dedicated for Xfce desktop environment.

%prep
%setup -qn %{name}-%{version}%{subrel}

%build
%configure2_5x \
	--enable-dpms \
	--enable-libnotify

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
%{_bindir}/%{name}*
%{_libdir}/xfce4/panel-plugins/xfce4-brightness-plugin
%{_libdir}/xfce4/panel-plugins/xfce4-inhibit-plugin
%{_datadir}/applications/*.desktop
%{_datadir}/xfce4/doc/C/images/*.png
%{_datadir}/xfce4/doc/C/xfce4-power-manager.html
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_mandir}/man1/*
