PGDMP  0                    |            database_in    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16445    database_in    DATABASE     �   CREATE DATABASE database_in WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE database_in;
                postgres    false            �            1259    16446 	   peramalan    TABLE     �   CREATE TABLE public.peramalan (
    "Settlement_Date" date NOT NULL,
    "Forecast" integer NOT NULL,
    "Amount_Per_Day" integer NOT NULL
);
    DROP TABLE public.peramalan;
       public         heap    postgres    false            �            1259    16449 	   transaksi    TABLE     �  CREATE TABLE public.transaksi (
    "Outlet_Name" character varying(255) NOT NULL,
    "Merchant_Id" character varying(225) NOT NULL,
    "Feature" character varying(225) NOT NULL,
    "Order_Id" character varying(225),
    "Transaction_Id" character varying(255) NOT NULL,
    "Amount" integer NOT NULL,
    "Net_Amount" integer NOT NULL,
    "Transaction_Status" character varying(225) NOT NULL,
    "Transaction_Time" timestamp with time zone,
    "Payment_Type" character varying(225) NOT NULL,
    "Payment_Date" date NOT NULL,
    "GoPay_Transaction_Id" character varying(125),
    "GoPay_Reference_Id" character varying(225),
    "GoPay_Customer_Id" integer,
    "Qris_Transaction_Type" character varying(225),
    "Qris_Reference_Id" character varying(225),
    "Qris_Issuer" character varying(125),
    "Qris_Acquirer" character varying(125),
    "Card_Type" character varying(125),
    "Credit_Card_Number" integer,
    "Settlement_Date" date NOT NULL,
    "Settlement_Time" timestamp with time zone
);
    DROP TABLE public.transaksi;
       public         heap    postgres    false            �            1259    16454    transaksi_Transaction_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."transaksi_Transaction_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public."transaksi_Transaction_Id_seq";
       public          postgres    false    216            �           0    0    transaksi_Transaction_Id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public."transaksi_Transaction_Id_seq" OWNED BY public.transaksi."Transaction_Id";
          public          postgres    false    217            �            1259    16455    user    TABLE     �   CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(125) NOT NULL,
    email character varying(80) NOT NULL,
    password character varying(255) NOT NULL
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    16458    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          postgres    false    218            �           0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          postgres    false    219            #           2604    16467    transaksi Transaction_Id    DEFAULT     �   ALTER TABLE ONLY public.transaksi ALTER COLUMN "Transaction_Id" SET DEFAULT nextval('public."transaksi_Transaction_Id_seq"'::regclass);
 I   ALTER TABLE public.transaksi ALTER COLUMN "Transaction_Id" DROP DEFAULT;
       public          postgres    false    217    216            $           2604    16460    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218            �          0    16446 	   peramalan 
   TABLE DATA           T   COPY public.peramalan ("Settlement_Date", "Forecast", "Amount_Per_Day") FROM stdin;
    public          postgres    false    215   \       �          0    16449 	   transaksi 
   TABLE DATA           �  COPY public.transaksi ("Outlet_Name", "Merchant_Id", "Feature", "Order_Id", "Transaction_Id", "Amount", "Net_Amount", "Transaction_Status", "Transaction_Time", "Payment_Type", "Payment_Date", "GoPay_Transaction_Id", "GoPay_Reference_Id", "GoPay_Customer_Id", "Qris_Transaction_Type", "Qris_Reference_Id", "Qris_Issuer", "Qris_Acquirer", "Card_Type", "Credit_Card_Number", "Settlement_Date", "Settlement_Time") FROM stdin;
    public          postgres    false    216   y       �          0    16455    user 
   TABLE DATA           ?   COPY public."user" (id, username, email, password) FROM stdin;
    public          postgres    false    218   *^       �           0    0    transaksi_Transaction_Id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public."transaksi_Transaction_Id_seq"', 1, false);
          public          postgres    false    217            �           0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 3, true);
          public          postgres    false    219            &           2606    16464    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public            postgres    false    218            (           2606    16466    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    218            �      x������ � �      �      x��}W�G��3�W�}Q��7|kO�ۑ�>����%��H��Q( U�B���g�"rr�ˊ�����ӫ�g?�����������/���)F��J���]�X���Pba������{��hZP�Ra���&q���!̔"�������������~V�A��#/�|!��=;r_>�~�����o�joF_�2����"��}uW�r<T0p$/<籈F�ę	�|>fь�K�Ѣ2}��A��?�C$�1�R��4�7?�O_�{u��xf$lʍ�H���i�pW�]�9x_�<��=�m-9<:�}�������ZƟ���	rs��<��Ag�	��	-��D�i���'�(���<q��~O?ݧ_��ۗ��O��%���	3��|M�̊:�C��9�0�L�a)j�Ì�A��U/�|�{Pm�v��e��cF��w4֪"$I�1�qC��Y4��r����_��{��@R-̭��w��+u��_�Ŋ��Wcn�����E;9�����V�`c��!u2�eB9�q�~!�u��w����Ys�_��s.�Ț��S&[�������q&^��M^p=3��ul��w.V&�Uamѯ�+�I��e���a>fQ} ��B�e��[��R
���9���<����}PD)��b�}X,�}:N�d��'�:�����W�%�r"����Ԇ��W$�PTr�d/ٔ��x7�!�D�gC�&��]GH�W)Ô	3�!$�lᦓ��N��n�<)����k!�[ǭ�(�ҍ5z�x��fr-�AH_K%��
�ah#� ]KE��3ʷ ����,q��^t݉���cD(�d1$D[��&=<�|!���}.�6c�q��D�t{x)�*�H � ����,�t��(�Wx"<�]��4���nl�������[���V,$`S�۶�M)SVj	*Ƞ��������U�|B���yAv������{D�]J�q�y[��2���g5(jJ�pV�NC��ݞ�R�p�ic=(��h�<hц"xb5�&�?��,����V�ȒW�bM��3�k.��D����/G�+Un�2J�͒^b��Z��O�=�:-�6g䉶�i5�a�D�i��1��4.���.	�sL�pڃ�L*|Ҽ��4,u����E3Q^
8*�m��� �!lp	]p�]ž~y���,�D��T4�%#���e7�\vr���y .�N�,C.�+��K0�"�Շ��%%QT�W\Rm����,�	T���"p&����9I��Z3����l��1s�4J�?�\n/v{!*��H���"W��3�j0��Q
2��> %���r��P6�|�����ˏ���A�4�ތz�ț��e�֠k.y}�ڠs"+AN\R[s�v�H4��f1��0�uc�t���(����=^��S�/�'4��A�{���x� |tBQ��0�F���f��e'�;}�7=�3ѠI�ZI��zFCԋ4���q0퍰�l�Axy�JG<��xD([���q�q��W^�VT��VY6s��n_�r�fOL�pQ �ZeуJFl �&
F�|̢����J�)����J�ix�����?�>[y��l�尛u�$�q�(�:��ԢUO����V�2�b��R:x��O-&Q�,ё�A+��DHixv@fK����n^U�-�LyT�A�(����9(�f|�TD�J}���n]w~��G��Z�G�Y�t���}ѳ�:*26�(��I�La3��ǃ� |qzW�IS���7��-��	��2E�������7���=�z�}�BvHPX�%�M2E�\
�j�ʈ�"����t�TD폰�L�=���޿��ΘU���F(�.��d���E�8�t�5�vB۱�n��u"|}��5~�dA֠g^��V#�*�$T�3n�MM;�eSV���õBx��T�k��p߬6	����^�@�h=������6�6R2!���LO���/�$�<�S�y��'�eb�jj#�����ҟ����ѻ�pT������QF*(���o�/��}('u~ȢTh�;��Ƙ^�R����`��V�ժ�����R	4�$�b(\�����M��$��Pt>fQ.�֨��
_���XQ�s5J ���˧��@��_@	<x'������WWV|����>~�#�N�p�Gj�vs��H}�|��35��,�7`��Rj��̺�ІL���O�������=:{_Fߝ��(Ĝۘu��H�t�EՎuȶ)��v�1x'�*��$jo��s#��� 4<�MI�\�!���IB� �?����{81��|YJ;����b�bNZ�{�fR����\Se^�1^̩�mu�-���CmX����Π=+�IR̄؆َK!��n�]
�l"HaVO��v��9��Q��gS��YTɯZ�ݴ��2��� �;�'G߿��o�t�I��_.��cv�٤������^p� �%�q*��:��,���Ȍ����OT�.�ͤ4ʗ%��
b���o_~99�xb�Zs�Nl����x-�=��"rvx��&Y�������HF�\�h���>���c|jtT|��\�:1ss�c�%��Tۘ���1 R�L<�2 �on�V���"Z T���
�5}�I�j+�2�d���{�b��Z^�l7��Dx���z���N�Mm6-���-���m�X~AǤN�\m���*j̆2�l�T4�+�l�1���
��p&�8c|+������*��N�jc3�[�u"��9�D9�R
)���|S>��)��"\l&TVQ���C�{#�6۱|�w"��'����y$��Bx���q�C��H���3 ,7�1Pt"<Q��({4��b��ohI��P;�g��PZЬf�g@Xm6�Dg�������\a#5E��+�A�d>fь�9e�(-t'h�_��:갪g�E�;�T����}=<����3�����bť�=~��S��!{��*�d�L�����F �^�_8��h1{�T7c4T	1Fd�Q��Z��w�ݠo8֥��ֹ7�}�u�*m�39`��D1�v<���f{��..1�!�&<��m��s/|�QG��gEax��./8U�����WW5�{Uִ)�����A���&�PМ��ye٠�V���/d�Ȟ�7��T�MŘ���5]������G�J6Kj���Y4�����N�e�����Uq���LS!�W��{zs��A�1�0�cF�WV^u��P�C�ԧ�����kTWLp�?�+��gH�S��SC���挆(6�x��Ѕy�4��W�6ff�JN�-�h�������YT6 ��(8i����,|�,�J����w���,���ͭȮZ.鵱׏i���k�Ĝ�|�5��L���hI`^;�x�������Ma�j��0�N���%�~����:�D=�Kxՠk�!���`:B�[��u"���M����:B|R�k(gnA�凝�yGݾʬ$����թ����'P>)�IҜ�|̢� �T������3i��KL��D���#������(�@��;?��W���l� 蛧2�E�G	ˢb���N�a��MJ%ڳ��M6���QI�tl���� |{s����`@YH�0�z�E�q!gj!+�M:��)YYo�G�m� �.�,*�L��Uoe�� �%�x� �t?B[F�IW�(�Am�f�
����28��y��ɥB�E�F�$�遈R��ш���l
�j��0W*/!�� z�DQ�/��"Ef.f��5��> mD����C��e��R^�s����?��|F�����f�I%�z���pDR��.xVm>��8��-� ����Hy=	�W7��J�ad}3��!��p\��7��58F����B�-�&����aU��vi-lTT����vL%a�/oxY��`�#���3�|ta0�"�ٮ��f��lމ�5}¤ �"Y)@(\�Kc&T3ohJ�e3Z��۳�pT�'c���T��PIL���[G(�	:FKu0 ��!Ե�q����Y��ʷ��    ;�'|��ی_5�1��c9����|ːհ���o' �7ۇo��O�e�0u f�B��Kڨ,�j�Ī�pڕ�<a������ci����D�ֆU&&���yȑƪ�p�l��v{!e'»�O'�&%utn&%��+J0���<'$!Qh�V!�g@Xm6!+%z��г�^+���d�b |>fQ]k��Vv2�LE0���U�3������\�|�F�0��LdX,��y�N��Q���	��3,x�R��y�i�R>E?T�� ��IR��%|���Ȱ�G�|����4�eY�DX�7L�L���x;��vF����l��Z���"��Ȁ��"�4�XD�c��<Iz>fQ� k-dg8VV�
Z;�V���F�q*��{ytq~����7�Qc��EX�9>��
�����x�o��14��Ąli���[�����aeV�]��IlQn�c/�U�o��ǂ`��g�4�w�`��ą6���0Q{G��f�c�=Z-,�<;�>fI�,���(g�3�O����9��3!��5�����G�.-���"�Bp����sF%��0�j�Ҫ�]i6lT̖���vL�S���[V&O��A�m�v+�^�h��9{r�pu�&�*R���m������)-�/=�bﹲ��]�m�&���:�<���DI�ɳSR��UA�TųA����l��,\���f���P=�L#��M�2z�!��&����&|+�f:SxKA�vY��HR����E�����Φ� ;H��);&��?���G���9��=>��m�j��Z���ZCΎ��mN�`O$�A�-lUD9�B�>e��cm����#O�-�Cc��u<J������uf;�)�Ϋtw��p�#ԃ�*}�;�照J2ɰ�-��A�+FeD�Q1f:�ߍOx'�w������@��*��]^���(���ɘ���K�O���3�K.�c�6;�M��Q�����|ƚ�a��ò���(%K!�g�����ˌ�+l
B>!��u"|<=.���F��l�J��z�B�8���
�+����LD��M��Z$�3��e*_��U�Y��Đ(v�&���,����H��!�.C6�m ���C������;����Uig
���C�6�%����kh���7<�Rߢ��i�Ѡ*��.GVQRǡ����Q��i\���f-"�o�����F���m3�NG�3�C]�E�=�u�*�Q�Zf;6ۣ�w��Z]<�&I^^�_�e`���SL��KI�P��
MJ����v�cg�oN�i�L��E��6[��C���)$�⸃�d�I���Q3���|�=f&#B���$a�zGJ�h��2!n6!����ż/g3�:cA*��^1���R��,��Ri"I���u��l�ɖi̂�M��Ǐ�38��������dj�1���/�v��ZM�_�8}8F� D%N�#��kq(c1�`���>�>Ψ�⣔�	�Ro��mP��ߝZ���<�p��0���,�J1vW��꜕2�Γ?t'����BI�r)#�r�YU��w����l7ϒ�D���b5��.�DQ��Bȳ�"�,��3>(�ѷ��Y����l7�ݪ��y�ҋ��J���$MҖ�H7���5Q�r=BS�\U��t'ޔ>���5`�E}���߅�=�Or�L��f_E�G�5q��۵'�D�Oޡt�R�l(����!Hd"p�`��{��MBXm6�ݥ�Jx�T�6O�`�[ƭTDY0h3�i>f�L�TM;�]��jF���][N���]K(堕�{�����{S%i����Œn3�.g���2}���޾Ū&f<��M� ����M�*��r}H<�"Jl7��y4ݘ�j�`~z����\j�/L�-̒f-��`zF�d��GE�������l����S�t��"�-�V'���Zڟl`�1@p�l��ODXm���DX���>�ˇ�ROf�5����E�Z����)d��'���kMv�����l�f�B����E�ܢ6-k!���V�\�r�Cg�͆1?a��>�y���F�NP�r�[��A�FƬ��S6�\Z͕Uv��y v�P���>���.n�]a9��t�;��\�3�������~i�^�8�o{q�D�l����ӧS���<Y��-<��+���L�To�'OOGhv����l�+�|�|������jn�q�Q4�0�� J��@����(�rs�}Z�,�;ǎ����Ϣ.Dh�����\)+�b`��٤%Q�h��w�ʷ0����~UUc�Aـ����IV3�EP�%��7>��o�Q�i:����o����&$m���Z!DUpO]ቷ��E�@����E�3K+*K[����K0�@K������?���z�@;Vsm�������_~������>�)�Ͽ�/�\���z��ձg��.IR�A0l�Nc�iM���幟�Y4�eWεb�G���S��t[�ao�PS��҉{����߾�Z�|���FT>�e�uJ�O��jQ�dt� 7"6C_�K%�3���23�u_�rDf�l��dG������5{�����&�ħ �T@̶�9k�4eA[50�E�x&#�҈6yg�f�}�*2���fx�"<+g� l>f�L6�z �'�u��; lv:��H]]����?�]o��)w�Eɮ���i������-��	�S����E`{�7\o*��%�8�t=K�:1�<J��;<���{���e9$��mCr��Cr;N��d�h�Z�0GweCWJ]Y?M[j��!Q���؀Wb�|��Qo��X���tP&�k��%Aй�DO8�{<0?ۂ��s;��)��v��N��C�A�Y�`w�^[��p)�U<Z�ՠک7OC���{�����_�=�Iv!xD�Z)��K�3�dТ-���,�gA����%��=,mv#�*�r�iåT�U-A��:|�Ζ��KŖ�<�G���+\˿bki7Ԙ���+����{MZi0�{w�ωp&-��e�Z�=g�$���b��ݯGw�A�}U۱�>��)����u�ܶ���6dCG��5)�d�7�t�Q�r Bk3�G-m\����+����s��ɂ�.1L4Ɓ���r�b��r<���^;�S�]v=nm�W�̅+_��/�Y�ع �B��\�{�F-��y~��*.0�6.���hM�,��=���t��XmI}LQ��7QMn��t�K������&� ||}���PR$"�-��f���끢��(���;�t
�j�	t
�`�vt�ʪ-����Ek���f?�h��V�iQ��Vta������
�~�qz"n�}}Z���q���z^-J�6�k8�>��A�00��I�n%GP�t.I�Ӑ5� jD�i<Ro�[PRvbVW��m�@�<)��C���hM�����K���A������vC�:�=��v(K�Dؾ�No2�Ǌ�-��s������l������1��8�R���F� {�����X�F����bc���QoG��������v{�*���@��EL	Ǎ3�n(�O<0)�>�l�cW�غ3ћSJ0��lz�� ����;>z��l � ؔu(�`���i��Z��ꃎ2{*SAH��:���$�4�R9*�|̢�A�-*+�w���{��׿ӿ��Q�k=4�a��/C����>��DcS�{�VPL3�=)$��u�8F�K�|�j^;�m���Uo�O;��2W/�J͐�B5h�'Z2���g���Q���گ51�K�k7#Q��9����s���A�������IW�tL�h����lǨ�z욓����f�N�H5 �m�V�d�t>�L�G�iY�G�f��i�+�&����~!i����XD�l�sSZS��YTW�1�� d,y��?Æ���*)XF�~�����>��r���H�v��<y�]�Ɩ=9v�1�1���ŖB2T���E[�Y������y�ő("�|����<wP�6��j%h7�\���Zv�!��n@��	�b�FJY�Ľ�̫��Ec8�T���81�:1�~z�����_裮Jy��p+�Ky�ά�f�^�*��v3���(O�-)���    »��|̢������R�������|x��e�eRW�j���%�L�) :%�ɛ;t%��ԁ�N�%�M4�9��f8��Ҽ��1�AT�����x}E�|v�
G�����[�h`	+��̂>��a�Stlف��>J�� BU���'D���J|m9ɪ0��B$�-������,�*<Tv�[��
o��Ͽ��/�5�~��~�<u��~#*���!��8��#���,�٩�_�"Jn���}<�惃fx��{��ka����mJ33�{Q�<�/�l��f{$G/>^��X^�d�B��}�#H�h��Q���W�F<��������q�G�Ԙo^�^�^D���`P)�[�A��Lbv9����n��A���1����?w{�}̧�������oU�*��]�Aj�et_�l�Н�?	!�P):�+�/�>�W�c��{�5�^ц��7y2�)s� E4-"�8����P�6�tn�|̢�,5)�V�L=s�u(�f�،�����+��Ão�O]?�|�6Ϋ�d�\��#�^ޔ���Ƞ�"G�eu�?
����Z�?�Q��$�D���x'������@���fjg�9���p� @�@���D�w�O����vl�O��	����X�}reu�˓LԾ`<e������������E�ͮnfcN�ۋs�"�q
��,0I�N�1����e�F�:�$vi���'8{2�^�ow}�{>���{n;(����'3TqttPv�v*8, 5�-�P�F��uJ�,ZZ�<s���M��*�h�<�jb3���oG��csP����7Β��1�jӌi��������M���­��`舿_~��\�C�1��8�`�����pF0��4-I�T��Q蘩d���,�F9������;�q^p%���7?�]��`0��0��C�Y����8����+�R:N1-/�!G��jt���u�0������.��iv9����~ݥ�x�Ӈ��#�9[H+���)͠�/��3�$�ڠ�����czI�e/��f;��%�ی�-@m�#�V�\�:C�1�@6�B�1�����ͼ�8^��!�>xz���w��Uy���H	�z(�>)�.r~w��n�L!G4<_r��X�`�0&�� ��2	�n0�������l�*��I	u�P	�y��g��I6<�)+]`C��Q�J�'a�&Lx'3VG�]����	�GЉ�!>h1�h��nC۴�_�r���#�ٛ�Gן�?���`tjp^%��bE��=��.qFF0�c�8���&��(�`+���E[ϫL��Y5���i*���ӏ�??��7Ǣ�Wt�8Rj�Jv�H)d+JX��s`汈*�h5N&��cmKϨ�����H�b�����Ƀ�����Kg�P3U�6I�W�O3�tT&�c$����=�-���J�1HvCV���1�
lT@'�}�+6���<��s�8�AƦ�L�Y���*�!g�?+�"��(g�n�.S���>M�?��˛�/l�^8M�m!dQ$:�L�V@4��,$�*�Q�f�6Ù��4S\���5&!�E	vCV 1�D��G�>�k0�@XU��?�j���Z�	���0y�iH�9Z
�ic8�~�
���
�)�U�)��`��5�i��V�ժ��v�R
l�2yƆ�`��ƫ0ng1UN��B$�9�h�˴)N1�m�zia�R(���6�����>]\��/��G<p=�ci!���WO��"U!�^��e&0���E�&Jl���#;�S�N���[,HZZ`��Y3�Q�-���,��z�w�t��َ�Ƶq������r�v.�׺�D,�$���E�㨖T�z���-���������럁���j�bE�Z�y^v�:�*���R�ǲ�����ۥ �̓���E�}�T��y^ry^B��|���ғF��!�Z)f󀪷�����q��P4����Ig''��{vp@�D�n��g������D�U��y���5';��*���G�i(+}�B�e�=�1K���� {̺��딌�� Y��lv�Mj��-�p!���Y4�X�Ru^
ֺ��/�~�%��m)D(6Vh��X1Z�4�L-�nx����bYҞh/�y�I	6��Rzۛ��&j�ft/�اf��V�>�`�2] �M�r�Pqr(H��m	�D�2}�ԳeVnO:�Vml�_���}��D?�I � 5͇1m�p<2�s�}& Uͥ�M��F!��M�h$+�A�Ao0���]��Fp�"u��j<�h0������m��Z.�:��6T܄���?n�Zz4(��ѨW�z46ά�f�w�����3h�%��W�)�p�A�)�Qlk��D>����)��j$v�c�Z���5XKZ�D��2��,�.������'��'�X��~������S���HCj�jJ&7��yD߾Ę4��I\�uQ�r���F���^����I��ǰ����ѹх�:L%jU0V3?�h��P�y3���UQKY��f5Dr�����#M��G=?���C�T15���+[f��h�9"C�4��=�X��n���`�=�'u���Lժ��&�c����]���D(��#d/��Y[7�h&J�S0e�O�o ����Y
C�T��:��])W�2���,V�ꌦ��ɍFj�����>�������ڐH`u�Y�S�*'�pU�׬q��L�j��f;��N�����r|��U�BE����z��j�,
�u��T�UM���A�?.U9�IT�еou�Rb,�]��A�U�:!ς��l��J�+j(��ф�{(�q�(�$9��X4�e��V`��A.�¤ټ�M~��2M����3����/Ƿh��Y�������߲ynK�&7��9��la�|L9#�9�f�h����z9�jr��Sx��~�v��Sb1U8+�C]y3�A��d��ZPQ�㍛�pJn������Q�Մ��@���*E�|̢��sX�M�����۽r(��)�	��}d?���J/��{~��4��6(���I�[py��gƩ/�^��D���0�z,��<�B�֬�
���,����`�G��cT �S/�ka�y23Fc�-���c�Y��{Jt"|}�=%�D����kC��נ�c�JA�<��Il䛡�I�CGw�)��+L���{����9��8�0�X��Y�-�RQ��Fu��=��ryD���{uxWY�����Ŋ>]v�Jv�b�����zbk�,��Kt�8�h�g��4$�����e`�ijo�>�^���~jY��?������]�"��4$��
�8Q�p�����rb>f�L�J��Rn��F*K�/���k�ŗ����A�~��|��)����t�8�x%�ږ�����c£ȅqD�
	� ����E[���.�e���B�خ]qq��pv���-�$z~y^����Z��]ݾ+3vd�U���!l	n��eב �W�U5n&v�J��9Iժ��&�(q(����ȉ҅�\��&�((Z�1��$T�f��*G��Gט3��ׇ��<g7��6Gt�8�#��)�`��ϑ�rD���,���O�|̢m�:Z���S���b�#�������w���?W�V3�DJ;УkeU��vnK��j��M:����	��tlݿ�IL7��L�!���	y�l���z����iE� <z��@	g:���0i#!'�ߣ�M����a/�{u�m0����=@�!�c6ޑlL���Q�Qۇ�y�>�k��5�G~��F͓6��B%e�ou�*cm�we�iuG�zD�\�jc��v։�]��	mܳ��W�4��lu�3�A�<(}=q+�P�6����ck�H�Y �;I
�.x�SӅ�D(��A�hs�[�9�U��V�Mx��)	�q�*`^��
���&���YT��PV�NȬ�T��w��E�þ������?���/L�"Z`-�P.�bI���Իm�25u�6�I�ˆ�`�`�^��X�XZ��_Q��lo���xG���a����(�NL T}gBQfi{P    ���:%��c_P)xW���-�D���>����ߘ�k��A`�
����Z���7�uh9S�3F9Sg�e��!g���[�B��/b���Q��1��E�<9�
SK&����Y
���i��i����1�f�t�h���!Ⱥ�����H�?�_ϯ~�=��|)/�g&����(ǯ�܃j�Mh<�i�I�$���1u7<[!j�r4�Ov�� :1�\�S�\��%b���G�e&Τ܆�l�������@�|��9,|���8�!�{i�t>fѶ�<+g�J�Q.Y���	�����x�ʼ�~�r9u�8�`^;�%%���&�G=���(hS$e���D���,�f0�r&�n慯*"JhJ_���|uz���c|blY>*�@lk��'�"g]�-2��{�}XE#'	�Q��k��ˈ+�J��+��P#��U�O��d�,kWHz(��S(�ٴ�@U��1���
���!�j���T�[a������A>�z^��46#�z�/��3Jǡ�3w|�(�^����4����o�i��ܥ��s��ޘ5�-��k2.kR���kt1BC�&�.&|���$jkA��C���L��~�!����f;�8�N�g��Li���xC@Z���� M$q��2�GmT�NEXm6!�#����@n9� ��N��8NT��1���**���
��Y�	 ����_�~�x�_��̮G����%vqZ�.ʜFQ�RA��H �GY�ƅ(�|�"���E-���d��DN:�m�<l� 1~�������K'3�gC8иWV�9���h�$+����&�1N��>~��p:QEo���1�fC-��T��i�yn�unT��k�����/�س�ͭ�R+Ɵ��}˚bup�3R�J�
�4kI̓ҙ
-�a���Q��7�8٨b����qW��<�(G�`�Ꚁ�����,b_�|y!�3�)R1�Ie*�u#<�`�V	Z�D!��!X�����,���6*8���K�z�eL�- 3�u��~|����q���Ǒ�V�P2�No�����9q�}���E۟��Қ�,�3�F�eFڮ�r6��`a�َ:T�v:I*E��Hnqb�(h�Zrl9��c�S�$U��=�:��Z�U�P�q����?�H�m�#6��|1�v��h8���ᶜ��t�8"��j���h��}��c
{x�&��Mjlo�\���~/�sQ|��-��C�^�c\E)9�2���Zm��7���M0+�7&�	��y�����M-�3�$	�R#͘�U8Je�ѩ�#��f,�o`�8�����~r�(1L���R�ʰ\�&Q=�L�Մ|����d\�eK��r7"��K�1�1
Rū���(��{d/,@\H4�h">�Ph��%W�������L�g�WDq��'{:B�l�l�By�s	��=��p��J�+�$\p����|V�_q�1�x*�r3>��d�Fd�D{,���`��\������1��:"�qߺ�$�v���k*�����߮<��Vne�#A�C��~\MM�.��ʄr�<���d���Y��B���%��U��t�ĨT���َ�7���ȜG�I8���2C�@��4{&���Y��/QGɦ:�%��[ʤ!����}8|����?�F��v�%�����2U6���	4D�8,F%������������ĉQ�'Vh�pI�i'��gX�&�AA)��L)��'l6�f|@��z��������vC�;��8;0�U9"-�Z�������JVf����I��y]$z�b,�"A%��_�I�:���cm��j����M�d���;��ۿO�'�-��eyӭ�J��K�n:'=�L���8������p˽����V��p	2��a�?���~���Jn�����害�h'�����bG0�Wk-\"�)s��`{R����bE�6������H;6��f/ �[�mʳ�L:N�!�u��hӐ%[������ٵ�^Ռ�d����k89�	��y��cb���Y���FE���+0��NZKK����K��|��vu�8N��8/�sb�*�7���M��`��;_e^���fZ�����|9��Y8��l����۳�Q���"�p<G�	�Y糄�N��s�n�?�z�	<$���{x%�s�Џ'��G*������,ڦ�rZ�^���"�סr8iP�9������?����`"
Ep�@������ڹ-)ڹ�c�
t�D����&S$�?��Tl>f�6�xM%�S��l����Ż�������e�m�����G� c�a�ы��v6�V�ePd>fѰ|�i����w��5gFI��$	�w�����P�:4�~��[s*�G�i�ڐ��R�+��0'�b�g��$M�)a*K�p!���Z�'��*��m����\��ل��:��"�m<����D�7��`�R����Y4|�(���&|cpF�[�M��qA.?�׿%����Cp��c�\�l�צd��V����-����0����@19������R=�s�#Fdxl �6��/�@x�������	�[@�Z�tYEεs�_�h���φ7��-��:Z8˰؅8��)��m�A0��,��hҨ�Rc��o�l-1���?߸o��<v���D`���w��W�Zv�̝��b��OZx�������aa>fѰ��i°Q\��5Y,�����}����p���,�^5pb�%}'�(�_�eji�o���}���˱��Ѷ_�rB�6�G8��I��dݎf����'��Q<��xyvP:�\�b�̈́�,�"&��3��T����vaDhu"�j�	ϥ�J9%�0��a�6'A*�_�ĭOa>fQ} Z
ea���E�N��������TŎnsb���Ŋ�ۮ�����g�m��ۇ�eC}�$��1�6���$�DbV����H)�)����݂Q�	���S� �����S��$i!s-��f�<�1�{a]��n�NCXo���p����b��{a`S�N�B�{��,AYWF�"��IZ�#,7�1��w"��a�eo��@86io!L8)��h��b��b�g@���S2�IH9{�uI��&Ϊ�<��6���]e��:
��Ԏ�u@�l
r���[�f Ïra(����{z�����*s�n5��s����f��5W<��r�nN�=���q>9Ŋ,VX�D��M��*��>�¼��m���T��$�\�9V�F��k���.���]R�#��� y'�����r*v6N���B�3Ӊg�n�پ��QS66B�V�MH��ё�)t��� &��>�M(��6b>fQ=�1�;�hُ���6�<���Q�Fa`��z�턜��/���lm7��i-ꩿ��Am���{�܊1^_��Cn��6�# �o1��2%����$��)/ьa��lW+��g��آt��)�I.����z8���E��-*�zE�&���<��U���_q�PM����3�rI�]�qb;����\rM��Q�����5.�`Gv'g|PUX�=kb.��7&F��,B��F*0j2�$X����Y4���)��%|���%r�%���u�D��b_�$�l(�,z�� ����Ql�����;y���Ԡi��"��~Lh�ؘ��ޘt�(�=�r"���ð��*:1�=1�t>$ixF̩��Z�m
�vXiR��b���]o�U+M��:P�0��R�flv�tř�˹�eo#���l�KG5J��FI��vlf���BH�z��T�Z�#��=""�N!�����h[>!�u|ծ�hI��a΁�c�v�`�̘�6o\=�h8��Rt�8��q�r	�ś��_>���@�83�o��&Rp����^�\a[\���^Rf���ծ���'u� ܟ+؋�����ta,
�fY�-<qF59��a�8�>�qC��rJBS��E���A�Z���N�o�/Xٲ�%&�M�fG�/�Xε�A9���Ş�r�����lB�@N��\K��W�������٫��ЏۢU��ߌ�,�Vto�Lw{팖�L�xS��m��Be�63���-.�3Dm����Ɍa� �  �]f�ntٍ��ل(`�kh"�A>�o:<\�U.��q+TT���e��lpk��-���\,�u6OH��Fm�;V���/�����?&�kLӯ���%�Q��_H�"�#<�ĮU����C����ZG�4`˜✯QGYs�1OiL^'0��'����/�GO�c��?n�lTuD��f�f��#��oWV�Yo]�c�{��U��/O��֙�{l��IJ�ԙ��&�m�F���x��l�f�փ��|w�PͿΎ���YG�b2����_��,������~�9�fu���&��2�`��Eϖ2��+ǰ�^���ހ(j:[�NC��M�,nΝ�L��ߟĻoB�o|Ǐ�:ǥ�Ajƛ��� 5���:Řl��X����Z�w&��Sq�S\��-�h���E����ĀU�:/�S\����tT'�̸������8(�`�Z����3���,���~��C=���.�V��A��3ڛ푫����Z�'"�etX�4?�"�"c�+˹�](�Y9q�k���.��6۱�w��A������5
��.�u̵�fj@v�D����9��˵�;zT��;D�@P�RDH[	�*R��j�.���<MD���It"$�w��ÌIq�!oCho��t�bYB��?�j�;��N�O'ט@B�����X"t�_ǐ�r�jU���\q��n�Pu"�>{_�CƝ���#�9+�b�#��D=��Y�f��C݉���(}}�KI���6�.<3��Ե��q�}��&rqt{�����V!A5�<�"X(E�M��__z]�c�&�eۄ�f�t�Z�f�1vɽ���h2�B��p��p%���YZ�r�ӧ3a����Y㑾>6�#,�@��0�IU�Y�BqF�`6��0]g�u��Qi�77���i�Sk��$�����������.���V]��������o�L�K�C��v�Mּ��pa$a����liHT#f���(1ʊ�����tm0�{QVmD�(�k���Yg	�0h�c%D�ڂy����ޯ��6�"pX���&��á���P
,LO�eB��3uLg��l��l�~L�7�N�,[�6 B�B�t�*��u��|.�S�9�d�z�R�����?��?�㛔�      �   �   x��=O�@ �9����}������X�q'*��ڠ
~=�ߣ�r�\a��}������_�t�����6�E8�n�g�9���<�:��bxJ�	���1�AO.MshU�{�F��$��u8�d��uODT ���Q�|43ر9�ةP�?�	���q����6�     